FROM php:7.2-fpm-alpine  
  
LABEL maintainer="Euan T"  
  
COPY conf.d/* /usr/local/etc/php/conf.d/  
  
RUN apk add --no-cache bzip2-dev libbz2 zlib-dev  
RUN docker-php-ext-install bz2 mysqli opcache pdo_mysql sockets zip  

