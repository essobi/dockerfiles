FROM composer  
  
FROM php:7.2-fpm-alpine  
  
LABEL maintainer="pierstoval@gmail.com"  
  
# Composer is always used as root in our container  
ENV COMPOSER_ALLOW_SUPERUSER=1  
RUN apk add --no-cache --update libpng-dev libjpeg-turbo-dev icu-dev
imagemagick \  
&& apk add --no-cache --virtual .build-deps $PHPIZE_DEPS \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure pdo_mysql \  
&& docker-php-ext-configure zip \  
&& docker-php-ext-install opcache intl pdo_mysql zip \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu gd intl pdo_mysql zip \  
&& echo "date.timezone = Europe/Paris" > /usr/local/etc/php/conf.d/custom.ini
\  
&& echo "short_open_tag = off" >> /usr/local/etc/php/conf.d/custom.ini \  
&& echo "apc.enabled = 1" >> /usr/local/etc/php/conf.d/custom.ini \  
&& apk del .build-deps  
  
COPY \--from=composer /usr/bin/composer /usr/local/bin/composer  
  
WORKDIR /var/www/html  

