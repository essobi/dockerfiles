FROM php:fpm-alpine  
  
MAINTAINER Trung Pham <pham.bao.trung@gmail.com>  
  
RUN apk update && \  
apk upgrade && \  
apk add libjpeg libjpeg-turbo libjpeg-turbo-dev libpng libpng-dev freetype
freetype-dev libmcrypt libmcrypt-dev yaml-dev libxml2-dev && \  
docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
pecl install apcu-5.1.7 && echo "extension=apcu.so" >
/usr/local/etc/php/conf.d/apcu.ini && \  
pecl install yaml-2.0.0 && echo "extension=yaml.so" >
/usr/local/etc/php/conf.d/yaml.ini && \  
docker-php-ext-install mcrypt zip gd opcache mbstring xml  
  
RUN apk del libxml2-dev libmcrypt-dev freetype-dev libjpeg-turbo-dev libpng-
dev yaml-dev  
RUN apk update && apk add libxml2 libmcrypt freetype libjpeg-turbo libpng yaml  
RUN rm -rf /var/cache/apk/*

