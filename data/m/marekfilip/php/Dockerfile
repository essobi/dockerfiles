FROM php:7.1-alpine  
  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps autoconf gcc g++ make \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug.so \  
&& apk del .build-deps  
  
ENV PHP_IDE_CONFIG "serverName=docker"  
ENV PHP_XDEBUG_ENABLED 1  
ENV XDEBUG_CONFIG remote_host=172.17.0.1  
COPY xdebug.ini /usr/local/etc/php/conf.d/  
COPY php.ini /usr/local/etc/php/

