FROM php:7.0-fpm  
  
# Copy the docker-php.ini config file  
COPY docker-php.ini /usr/local/etc/php/conf.d/docker-php.ini  
  
# Update apt-get  
RUN apt-get update  
  
# Nano (texteditor)  
RUN apt-get install -y nano  
  
# Wget  
RUN apt-get install -y wget  
  
# Git  
RUN apt-get install -y git  
  
# MySQL  
RUN apt-get install -y libmcrypt-dev mysql-client zlib1g-dev && docker-php-
ext-install mcrypt pdo_mysql  
RUN docker-php-ext-install mysqli  
  
# Zip Unzip  
RUN apt-get install -y zip unzip zlib1g-dev  
RUN docker-php-ext-install zip  
  
# GD  
RUN apt-get install -y libjpeg-dev  
RUN apt-get install -y libfreetype6-dev  
RUN apt-get install -y libpng-dev  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install gd  
  
# Moodle-specific  
RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev g++ libxml2-dev  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install xmlrpc  
  
# Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  

