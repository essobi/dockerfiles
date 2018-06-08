FROM php:fpm-alpine3.7  
  
MAINTAINER Loup-des-Neiges <contact@loup-des-neiges.com>  
  
RUN set -eux; \  
apk add --no-cache freetype-dev libjpeg-turbo-dev libpng-dev; \  
docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/
--with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/; \  
docker-php-ext-install gd mysqli opcache zip exif  
  
COPY opcache-recommended.ini /usr/local/etc/php/conf.d/  

