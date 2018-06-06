FROM php:7.1.15-fpm-alpine  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN set -x \  
&& apk add --update --no-cache libmemcached freetype libpng libjpeg-turbo icu
libxml2 git c-client \  
&& apk add --no-cache --virtual .phpize-deps $PHPIZE_DEPS \  
zlib-dev libmemcached-dev cyrus-sasl-dev openssl-dev libxml2-dev freetype-dev
libpng-dev libjpeg-turbo-dev pcre-dev imap-dev icu-dev \  
libtool python \  
&& echo \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& echo \  
&& ( \  
git clone https://github.com/edenhill/librdkafka.git /usr/src/librdkafka \  
&& cd /usr/src/librdkafka \  
&& ./configure --prefix=/usr \  
&& make -j "$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
&& rm -rf /usr/src/librdkafka \  
) \  
&& echo \  
&& git clone https://github.com/arnaud-lb/php-rdkafka.git
/usr/src/php/ext/php-rdkafka \  
&& docker-php-ext-configure /usr/src/php/ext/php-rdkafka \  
&& docker-php-ext-install /usr/src/php/ext/php-rdkafka \  
&& rm -rf /usr/src/php/ext/php-rdkafka \  
&& echo \  
&& docker-php-ext-install pdo_mysql intl zip sockets soap exif \  
&& echo \  
&& git clone -b php7 https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached \  
&& docker-php-ext-configure /usr/src/php/ext/memcached --disable-memcached-
sasl \  
&& docker-php-ext-install /usr/src/php/ext/memcached \  
&& rm -rf /usr/src/php/ext/memcached \  
&& echo \  
&& docker-php-ext-configure imap --with-imap --with-imap-ssl \  
&& docker-php-ext-install imap \  
&& echo \  
&& pecl channel-update pecl.php.net \  
&& pecl install xdebug mongodb redis apcu msgpack \  
&& docker-php-ext-enable mongodb opcache zip redis apcu sockets gd msgpack
intl rdkafka soap exif \  
&& echo \  
&& apk del .phpize-deps \  
&& echo \  
&& touch /usr/local/etc/php/conf.d/xdebug.ini \  
&& chmod a+w /usr/local/etc/php/conf.d/xdebug.ini \  
&& php -r "readfile('https://getcomposer.org/installer');" | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& echo \  
&& mkdir /app \  
&& chown 1000:1000 /app \  
&& echo  
  
COPY entrypoint.sh /  
COPY etc/* /usr/local/etc/php/  
  
EXPOSE 9000  
ENTRYPOINT [ "/entrypoint.sh" ]  
WORKDIR /app  
ENV HOME=/app  
USER 1000:1000  

