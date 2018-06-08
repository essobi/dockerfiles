FROM php:rc-fpm-alpine  
MAINTAINER benedikt.franke@twofour.de  
  
ENV PHP_MAX_EXECUTION_TIME=240  
ENV PHP_MEMORY_LIMIT=128M  
ENV PHP_MAX_INPUT_VARS=4096  
RUN docker-php-ext-install \  
pdo_mysql \  
mysqli  
  
COPY content /  
  
WORKDIR /var/www/html  

