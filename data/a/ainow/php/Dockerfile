FROM php:7.2.1-fpm-alpine3.7  
MAINTAINER coolbaby "coolbaby"  
  
RUN \  
pecl channel-update pecl.php.net \  
&& apk add --no-cache --virtual .phpize-deps $PHPIZE_DEPS linux-headers zlib-
dev \  
&& apk add --no-cache --virtual .yaf-swoole linux-headers zlib-dev \  
&& pecl install yaf swoole\  
&& docker-php-ext-enable yaf swoole \  
&& apk del .yaf-swoole \  
# install bz2 ext  
\  
&& apk add --no-cache --virtual .bz2 libbz2 bzip2-dev \  
&& docker-php-ext-install -j$(nproc) bz2 \  
\  
# install gd ext  
\  
&& apk add --no-cache --virtual .gd freetype libpng libjpeg-turbo freetype-dev
libpng-dev libjpeg-turbo-dev \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--enable-gd-native-ttf \  
&& docker-php-ext-install -j$(nproc) gd \  
\  
# install gettext ext  
\  
&& apk add --no-cache --virtual .gettext gettext-dev \  
&& docker-php-ext-install -j$(nproc) gettext \  
\  
# install mcrypt ext  
&& apk add --no-cache --virtual .mcrypt $PHPIZE_DEPS libmcrypt-dev \  
# from php7.2 mcrypt remove to pecl  
\  
&& pecl install channel://pecl.php.net/mcrypt-1.0.1 \  
&& docker-php-ext-enable mcrypt \  
\  
# install memcached ext  
\  
&& apk add --no-cache --virtual .memcached libmemcached-dev cyrus-sasl-dev \  
&& pecl download memcached-3.0.4 \  
&& mkdir -p /tmp/memcached \  
&& tar xf memcached-3.0.4.tgz -C /tmp/memcached --strip-components=1 \  
&& docker-php-ext-configure /tmp/memcached --with-libmemcached-dir=/usr \  
&& docker-php-ext-install -j$(nproc) /tmp/memcached \  
&& rm -rf memcached-3.0.4.tgz \  
&& rm -rf /tmp/memcached* \  
\  
# install redis ext  
&& pecl install redis-3.1.6 \  
&& docker-php-ext-enable redis \  
# install mongodb ext  
\  
#&& apk add --no-cache --virtual .mongodb openssl-dev \  
&& apk add --no-cache --virtual .mongodb libressl-dev \  
&& pecl install mongodb-1.3.4 \  
&& docker-php-ext-enable mongodb \  
\  
# install pdo pdo_mysql pdo_pgsql pgsql mysqli ext  
\  
&& apk add --no-cache --virtual .db postgresql-dev \  
&& docker-php-ext-install pdo pdo_mysql pdo_pgsql pgsql mysqli \  
\  
# install pcntl,soap,sockets ext  
\  
&& apk add --no-cache --virtual .others libxml2-dev \  
&& docker-php-ext-install pcntl soap sockets \  
&& apk del .others \  
\  
# install apcu ext  
\  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
\  
&& rm -rf /tmp/pear ~/.pearrc \  
&& apk del .phpize-deps \  

