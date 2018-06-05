FROM php:5.6-fpm  
MAINTAINER Jean-Yves CAMIER <jycamier@clever-age.com>  
  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime  
RUN "date"  
  
# base path for extension  
RUN mkdir -p /usr/src/php/ext  
  
# ACPU installation  
RUN curl -L -o /tmp/apcu-4.0.7.tgz https://pecl.php.net/get/apcu-4.0.7.tgz  
RUN tar xfz /tmp/apcu-4.0.7.tgz -C /usr/src/php/ext  
RUN mv /usr/src/php/ext/apcu-4.0.7 /usr/src/php/ext/apcu  
  
RUN apt-get update \  
&& apt-get install -y \  
libicu-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install \  
apcu \  
intl \  
mbstring \  
mysqli \  
pdo \  
pdo_mysql \  
exif \  
zip  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www/symfony

