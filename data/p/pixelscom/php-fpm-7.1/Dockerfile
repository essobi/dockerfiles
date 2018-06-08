FROM php:7.1.11-fpm-alpine  
  
MAINTAINER Bill Hance <bill@hance.io>  
  
ENV PHP_DISPLAY_ERRORS Off  
ENV PHP_MEMORY_LIMIT 1024M  
ENV PHP_PHP_MAX_EXECUTION_TIME 30  
ENV PHP_MAX_INPUT_TIME 60  
ENV OPCACHE_MEMORY_CONSUMPTION 128  
ENV OPCACHE_MAX_ACCELERATED_FILES 20000  
ENV OPCACHE_REVALIDATE_FREQUENCY 120  
RUN set -xe \  
&& apk add --no-cache \  
icu-dev \  
libxml2-dev \  
tzdata \  
&& docker-php-ext-configure opcache --enable-opcache \  
&& docker-php-ext-install \  
bcmath \  
intl \  
opcache \  
pdo_mysql \  
zip \  
&& cp /usr/share/zoneinfo/UTC /etc/localtime \  
&& echo "UTC" > /etc/timezone \  
&& "date" \  
&& apk del tzdata \  
&& rm -rf /tmp/* /usr/local/lib/php/doc/* /var/cache/apk/*  
  
RUN docker-php-source extract \  
&& apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
&& apk del .phpize-deps-configure \  
&& docker-php-source delete  
  
COPY php.ini /usr/local/etc/php/conf.d/user-defined-php.ini  
COPY opcache.ini /usr/local/etc/php/conf.d/user-defined-opcache.ini  
COPY intl.ini /usr/local/etc/php/conf.d/user-defined-intl.ini  
  
WORKDIR /app  

