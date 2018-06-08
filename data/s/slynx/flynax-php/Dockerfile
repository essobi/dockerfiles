FROM php:7.2.1-fpm  
  
MAINTAINER scurow  
  
RUN apt-get update && apt-get upgrade -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmagickwand-dev \  
libpng-dev \  
libmemcached-dev \  
libicu-dev \  
g++ \  
&& docker-php-ext-install \  
iconv \  
mbstring \  
mysqli \  
pdo_mysql \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl \  
&& yes '' | pecl install imagick && docker-php-ext-enable imagick  

