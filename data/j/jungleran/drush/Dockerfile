FROM jungleran/drupal-base:8.5.3-apache  
  
MAINTAINER Jungle Ran <jungle.r@intergreat.com>  
  
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
  
RUN echo "memory_limit = -1" > /usr/local/etc/php/conf.d/custom.ini \  
&& echo "error_log = /var/www/html/logs/php_error.log" >>
/usr/local/etc/php/conf.d/custom.ini \  
&& echo "log_errors = On" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "upload_max_filesize = 256M" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "post_max_size = 64M" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "max_execution_time = 600" >> /usr/local/etc/php/conf.d/custom.ini  
  
# Update the entry point of the application  
ENTRYPOINT ["drush"]  

