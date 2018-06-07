FROM jungleran/drupal-base:8.5.3-apache  
  
RUN echo "memory_limit = -1" > /usr/local/etc/php/conf.d/custom.ini \  
&& echo "error_log = /var/www/html/logs/php_error.log" >>
/usr/local/etc/php/conf.d/custom.ini \  
&& echo "log_errors = On" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "upload_max_filesize = 256M" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "post_max_size = 64M" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "max_execution_time = 600" >> /usr/local/etc/php/conf.d/custom.ini  
  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
RUN echo "xdebug.remote_connect_back = 0" >>
/usr/local/etc/php/conf.d/custom.ini \  
&& echo "xdebug.remote_host = 10.0.2.2" >>
/usr/local/etc/php/conf.d/custom.ini \  
&& echo "xdebug.remote_port = 9000" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "xdebug.idekey = PhpStorm" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "xdebug.remote_enable = 1" >> /usr/local/etc/php/conf.d/custom.ini  
  
ENV DRUPAL_CONSOLE_ALIAS dp  
  
RUN echo "alias $DRUPAL_CONSOLE_ALIAS=\"cd /var/www/html/web;
../vendor/bin/drupal\"" >> ~/.bashrc  
  
# Add common extensions  
RUN apt-get update && apt-get install -y mysql-client  
RUN docker-php-ext-install pdo_mysql  
  
# Set the Drush version.  
ENV DRUSH_VERSION 8.1.16  
# Install Drush 8 with the phar file.  
RUN curl -fsSL -o /usr/local/bin/drush "https://github.com/drush-
ops/drush/releases/download/$DRUSH_VERSION/drush.phar" \  
&& chmod +x /usr/local/bin/drush  
  
RUN drush --version  

