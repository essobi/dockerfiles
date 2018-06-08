# Start with the official php-5 with apache  
FROM php:7-apache  
  
MAINTAINER Us Media <info@usmedia.nl>  
  
#  
# Install Dependencies & Build PHP Extensions:  
# opcache, mbstring, iconv, mcrypt, mysql, GD, intl  
#  
RUN apt-get update && apt-get install -y \  
locales locales-all \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libicu-dev \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install iconv \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install pdo_mysql mysqli \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& rm -rf /var/lib/apt/lists/*  
  
#  
# Install xdebug (todo: make this runtime configurable)  
#  
RUN pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
#  
# Enable apache mods  
#  
RUN a2enmod rewrite deflate expires  

