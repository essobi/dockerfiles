FROM php:7.0.11-fpm-alpine  
  
# Installations extentions necessaires  
RUN apk add --no-cache freetype-dev freetype && \  
docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ && \  
docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) gd mysqli pdo pdo_mysql
&& \  
apk del --purge freetype-dev  

