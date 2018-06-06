FROM php:fpm  
MAINTAINER Danillo Nunes <marcus@danillo.net>  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
&& \  
  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd mbstring pdo pdo_mysql && \  
  
rm -rf /var/cache/apk/*  
  
CMD "php-fpm"  

