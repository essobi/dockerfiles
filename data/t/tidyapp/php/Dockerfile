FROM php:7-fpm-alpine  
  
RUN apk add --no-cache --virtual .build-deps \  
zlib-dev  
  
RUN docker-php-ext-install \  
pdo_mysql \  
zip  
  
RUN apk del .build-deps

