FROM unitedasian/nginx:alpine  
  
MAINTAINER Olivier Pichon <op@united-asian.com>  
  
ENV PHP_INI_DIR /etc/php  
  
RUN apk add --update \  
php-fpm \  
php-cli \  
php-curl \  
php-openssl \  
php-phar \  
php-zip \  
php-zlib \  
&& rm -rf /var/cache/apk/* \  
&& echo "memory_limit=${PHP_MEMORY_LIMIT:--1}" > $PHP_INI_DIR/conf.d/memory-
limit.ini \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
COPY supervisor.d/php-fpm.ini /etc/supervisor.d/php-fpm.ini  
  
COPY php/php-fpm.conf /etc/php/php-fpm.conf  
  
COPY php/pool.d /etc/php/pool.d  
  
ONBUILD COPY nginx/conf.d /etc/nginx/conf.d  
  
ONBUILD COPY . /var/www  

