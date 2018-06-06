FROM php:5.6-apache  
  
ENV DEBCONF_FRONTEND non-interactive  
  
RUN apt-get update && apt-get install -y vim git imagemagick libcurl4-openssl-
dev libfreetype6-dev libjpeg-turbo-progs libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev libxml2-dev mysql-client pngquant ssmtp sudo unzip wget
zlib1g-dev  
RUN docker-php-ext-install bcmath exif curl mbstring mcrypt mysql mysqli
opcache pcntl pdo_mysql soap zip  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
  
ADD bin/docker-php-pecl-install /usr/local/bin/  
  
RUN docker-php-pecl-install memcache uploadprogress xdebug  
  
RUN pear install PHP_CodeSniffer  
  
RUN echo "sendmail_path = /usr/sbin/ssmtp -t" >
/usr/local/etc/php/conf.d/conf-sendmail.ini  
RUN echo "date.timezone='Europe/Paris'\n" > /usr/local/etc/php/conf.d/conf-
date.ini  
RUN echo "memory_limit = 512M" > /usr/local/etc/php/conf.d/conf-memory.ini  
RUN echo "max_execution_time = 60" > /usr/local/etc/php/conf.d/conf-execution-
time.ini  
  
RUN cd /usr/local \  
&& curl -sS https://getcomposer.org/installer | php \  
&& chmod +x /usr/local/composer.phar \  
&& ln -s /usr/local/composer.phar /usr/local/bin/composer  
  
RUN cd /usr/local \  
&& git clone http://github.com/drush-ops/drush.git --branch master \  
&& cd /usr/local/drush \  
&& composer install \  
&& ln -s /usr/local/drush/drush /usr/bin/drush  
  
RUN curl https://drupalconsole.com/installer -L -o drupal.phar \  
&& mv drupal.phar /usr/local/bin/drupal \  
&& chmod +x /usr/local/bin/drupal \  
&& drupal init --override \  
&& drupal check  
  
RUN drush dl coder --destination=/usr/local \  
&& ln -s /usr/local/coder/coder_sniffer/Drupal
/usr/local/lib/php/PHP/CodeSniffer/Standards/  
  
RUN rm -rf /var/www/html && ln -s /project/www /var/www/html  
  
RUN drush init -y  
COPY aliases.drushrc.php /root/.drush/aliases.drushrc.php  
  
COPY xdebug.ini /usr/local/etc/php/conf.d/conf-xdebug.ini  
  
RUN apt-get clean  
  
RUN a2enmod deflate  
RUN a2enmod expires  
RUN a2enmod headers  
RUN a2enmod mime  
RUN a2enmod rewrite  

