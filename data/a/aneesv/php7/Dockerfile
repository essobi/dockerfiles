################################################################################  
# Base image  
################################################################################  
  
FROM php:7.1-fpm  
  
MAINTAINER Anees v <mail@aneesv.me>  
  
  
################################################################################  
# Build instructions  
################################################################################  
  
# Sync apt  
RUN apt-get update \  
# Curl  
&& apt-get install -y libcurl3-dev && docker-php-ext-install curl \  
# GD  
&& apt-get install -y libpng12-dev libjpeg62-turbo-dev libfreetype6-dev &&
docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/
--with-png-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && docker-php-ext-
install gd \  
# Postgresql  
&& apt-get install -y libpq-dev && docker-php-ext-install pgsql \  
# Mcrypt  
&& apt-get install -y libmcrypt-dev && docker-php-ext-install mcrypt \  
# Mysqli  
&& docker-php-ext-install mysqli \  
# ImageMagic  
&& apt-get install -y libmagickwand-dev --no-install-recommends && pecl
install imagick && docker-php-ext-enable imagick \  
# JSON  
&& docker-php-ext-install json \  
# ZIP  
&& apt-get install -y zlib1g-dev libicu-dev g++ && docker-php-ext-configure
zip --with-zlib-dir=/usr && docker-php-ext-install zip \  
# PDO PDO Mysql  
&& docker-php-ext-install pdo pdo_mysql gettext intl \  
# Remove apt lists to reduce image size  
&& rm -rf /var/lib/apt/lists/*  

