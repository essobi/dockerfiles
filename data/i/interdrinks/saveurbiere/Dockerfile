FROM composer:latest as composer  
FROM php:7.0-fpm-alpine  
  
# https://getcomposer.org/doc/03-cli.md#composer-allow-superuser  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
COPY --from=composer /usr/bin/composer /usr/bin/composer  
COPY php.ini /usr/local/etc/php/php.ini  
COPY php-fpm.conf /usr/local/etc/php-fpm.d/php-fpm.conf  
  
HEALTHCHECK --interval=10s \--timeout=3s \  
CMD \  
SCRIPT_NAME=/ping \  
SCRIPT_FILENAME=/ping \  
REQUEST_METHOD=GET \  
cgi-fcgi -bind -connect 127.0.0.1:9000 || exit 1  
  
WORKDIR /var/www/html  
  
RUN set -xe \  
&& apk add --no-cache --virtual .persistent-deps \  
git \  
curl \  
icu-libs \  
zlib \  
fcgi \  
libmcrypt \  
libpng \  
libmemcached \  
libxml2 \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
icu-dev \  
zlib-dev \  
curl-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
libmemcached-dev \  
cyrus-sasl-dev \  
&& docker-php-ext-install \  
intl \  
pdo_mysql \  
zip \  
soap \  
curl \  
gd \  
mbstring \  
mcrypt \  
&& pecl install \  
apcu \  
redis \  
memcached \  
&& docker-php-ext-enable \  
apcu \  
opcache \  
redis \  
memcached \  
&& rm -rf /tmp/pear \  
&& apk del .build-deps \  
&& composer global require "hirak/prestissimo:^0.3" \--prefer-dist --no-
progress --no-suggest --optimize-autoloader --classmap-authoritative \  
&& composer clear-cache \  
&& mkdir -p var/cache var/logs var/sessions \  
&& chmod -R 777 var /tmp  
  
CMD ["php-fpm"]  

