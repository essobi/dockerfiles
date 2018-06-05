FROM php:7.0-fpm-alpine  
  
ENV PHALCON_VERSION=3.0.3  
ENV MEMCACHED_VERSION=3.0.2  
  
ENV PHALCON_DEPS autoconf g++ make git  
ENV MEMCACHED_DEPS libmemcached-dev zlib-dev cyrus-sasl-dev git  
ENV EXT_DEPS icu-dev  
  
# Basic extensions  
RUN set -xe && \  
apk add --update icu && \  
apk add --no-cache --virtual .ext-deps ${EXT_DEPS} && \  
docker-php-ext-install intl pdo_mysql bcmath && \  
apk del .ext-deps  
  
# Compile Phalcon  
RUN set -xe && \  
apk add --no-cache --virtual .phalcon-deps ${PHALCON_DEPS} && \  
  
git clone -b v${PHALCON_VERSION} https://github.com/phalcon/cphalcon.git
/usr/src/php/ext/phalcon && \  
cd /usr/src/php/ext/phalcon/build && sh install && \  
docker-php-ext-enable phalcon && \  
rm -rf /usr/src/php/ext/phalcon && \  
  
apk del .phalcon-deps  
  
# Install memcached  
RUN set -xe && \  
apk add --update libmemcached && \  
apk add --no-cache --virtual .memcached-deps ${MEMCACHED_DEPS} && \  
git clone -b php7 https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached && \  
docker-php-ext-configure /usr/src/php/ext/memcached --disable-memcached-sasl
&& \  
docker-php-ext-install /usr/src/php/ext/memcached && \  
apk del .memcached-deps && \  
rm -rf /usr/src/php/ext/memcached && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

