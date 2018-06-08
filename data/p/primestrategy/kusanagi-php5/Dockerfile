#//----------------------------------------------------------------------------  
#// PHP5 FastCGI Server ( for KUSANAGI Runs on Docker )  
#//----------------------------------------------------------------------------  
FROM php:5.6.26-fpm-alpine  
MAINTAINER kusanagi@prime-strategy.co.jp  
  
# Environment variable  
ARG MYSQL_VERSION=10.1.17-r0  
ARG APCU_VERSION=4.0.11  
  
  
RUN apk update \  
&& apk add --no-cache --virtual .build-php \  
$PHPIZE_DEPS \  
mysql=$MYSQL_VERSION \  
&& docker-php-ext-install mysqli opcache \  
&& pecl install apcu-$APCU_VERSION \  
&& docker-php-ext-enable apcu \  
&& apk del .build-php \  
&& rm -f /usr/local/etc/php/conf.d/docker-php-ext-apc.ini \  
&& rm -f /usr/local/etc/php/conf.d/docker-php-ext-apcu.ini \  
&& rm -f /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \  
&& mkdir -p /etc/php.d/  
  

