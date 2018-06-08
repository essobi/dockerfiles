ARG PHP_VERSION=7.2  
ARG ALPINE_VERSION=3.7  
FROM php:${PHP_VERSION}-fpm-alpine${ALPINE_VERSION}  
  
RUN set -xe  
RUN apk upgrade --update  
  
RUN apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
icu-dev \  
zlib-dev \  
imagemagick-dev \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
libssh-dev  
  
RUN apk add --no-cache \  
git \  
imagemagick \  
freetype \  
libpng \  
libjpeg-turbo \  
yarn \  
# for intl  
icu-libs  
  
ENV APCU_VERSION 5.1.11  
RUN pecl install apcu-${APCU_VERSION}  
RUN pecl install imagick  
  
RUN docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install exif  
RUN docker-php-ext-install bcmath  
RUN docker-php-ext-install sockets  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) gd  
  
RUN docker-php-ext-enable --ini-name 20-apcu.ini apcu  
RUN docker-php-ext-enable --ini-name 05-opcache.ini opcache  
RUN docker-php-ext-enable imagick  
  
RUN apk del .build-deps  
  
COPY php.ini /usr/local/etc/php/php.ini  
# COPY php-fpm.conf /usr/local/etc/php-fpm.d/99-overrides.conf  
ENV COMPOSER_ALLOW_SUPERUSER 1  
COPY \--from=composer:latest /usr/bin/composer /usr/bin/composer  
ENV PATH="${PATH}:/root/.composer/vendor/bin"  
# Speed up composer builds - concurrent requests  
RUN composer global require "hirak/prestissimo:^0.3" \--prefer-dist --no-
suggest --classmap-authoritative  
  
WORKDIR /srv/api  
  
RUN mkdir -p var/cache var/sessions var/log  
  
RUN chown -R www-data var  
VOLUME /srv/api/var  
  
EXPOSE 9000  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint  
RUN chmod +x /usr/local/bin/docker-entrypoint  
  
ENTRYPOINT ["docker-entrypoint"]  
  
CMD ["php-fpm"]  

