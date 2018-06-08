FROM php:7.2-fpm-alpine3.7  
MAINTAINER Tomas Leypold (tomas.leypold@nethost.cz)  
  
#phpize dependencies  
ENV PHPIZE_DEPS \  
autoconf \  
dpkg-dev dpkg \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c  
  
# php base extensions installation  
RUN apk add --no-cache libpcre32 re2c gettext-dev libpng-dev \  
&& docker-php-ext-install -j$(nproc) mysqli gettext gd pdo_mysql iconv \  
&& apk del libpcre32 re2c  
  
# pecl update  
RUN pecl channel-update pecl.php.net  
  
# phalconphp dependencies  
RUN apk add --no-cache zlib-dev libzip libzip-dev \  
&& docker-php-ext-configure zip --with-libzip \  
&& docker-php-ext-install -j$(nproc) zip \  
&& apk del zlib-dev libzip-dev  
  
# gearman php extension compile&install  
COPY apk/* /tmp/  
RUN set -xe && apk update && apk add --no-cache git coreutils \  
&& apk add --allow-untrusted /tmp/gearman-dev-1.1.15-r2.apk /tmp/gearman-
libs-1.1.15-r2.apk \  
&& mkdir -p /tmp/gearman && cd /tmp/gearman/ \  
&& git clone https://github.com/wcgallego/pecl-gearman.git \  
&& cd pecl-gearman \  
&& git checkout gearman-2.0.3 \  
&& docker-php-ext-install -j$(nproc) /tmp/gearman/pecl-gearman \  
&& apk del git \  
&& rm -r /tmp/gearman*  
  
# phalconphp, redis extension compile&install  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
&& curl -fsSL 'https://github.com/phalcon/cphalcon/archive/v3.3.1.tar.gz' -o
phalcon.tar.gz \  
&& mkdir -p /tmp/phalcon \  
&& tar -xf phalcon.tar.gz -C /tmp/phalcon --strip-components=1 \  
&& rm phalcon.tar.gz \  
&& docker-php-ext-configure /tmp/phalcon/build/php7/64bits --enable-phalcon \  
&& docker-php-ext-install -j$(nproc) /tmp/phalcon/build/php7/64bits \  
&& rm -r /tmp/phalcon \  
&& apk del .build-deps $PHPIZE_DEPS  
  

