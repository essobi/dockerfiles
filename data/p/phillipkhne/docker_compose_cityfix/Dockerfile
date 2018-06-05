#Aktuellstes Alpine-Linux Basisimage, deutlich leichtgewichtiger und sicherer
als Ubuntu, da speziell für Container gedacht.  
FROM php:7.1-fpm-alpine  
  
# Lumen-Abhängigkeiten installieren  
RUN apk update --no-cache  
RUN apk fix --no-cache  
RUN apk add --no-cache wget nano alpine-sdk bash  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install mbstring  
RUN php -i  
  
#composer installieren  
RUN apk add --no-cache curl  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
#lumen selbst  
RUN composer global require "laravel/lumen-installer"  
  
#xdebug  
RUN apk add --update --virtual --no-cache autoconf  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
# OpenSSH-Client (für Deployment)  
RUN apk add --no-cache openssh-client  
# rsync für deployment  
RUN apk add --no-cache rsync  
  
#memcached  
RUN apk add --update --virtual --no-cache zlib zlib-dev libmemcached
libmemcached-dev cyrus-sasl-dev cyrus-sasl  
RUN pecl install memcached \  
&& docker-php-ext-enable memcached  
  
# phpunit  
RUN wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && \  
phpunit --version  
  
# osmfilter  
RUN wget -O /tmp/osmfilter.c http://m.m.i24.cc/osmfilter.c && \  
gcc -x c /tmp/osmfilter.c -O3 -o /tmp/osmfilter && \  
mv /tmp/osmfilter /usr/local/bin/osmfilter  
  
WORKDIR /root/workspace

