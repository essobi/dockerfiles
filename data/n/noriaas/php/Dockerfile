################################################################################  
# Noriaas/php:latest tag  
################################################################################  
  
FROM php:7.1.12-fpm-alpine  
  
ENV XDEBUG_ENABLE=1 \  
XDEBUG_PORT=9000 \  
  
PHP_REDIS=3.1.4 \  
PHP_AMQP=1.9.3 \  
PHP_ACPU=5.1.8 \  
PHP_EVENT=2.3.0 \  
PHP_IGBINARY=2.0.5 \  
PHP_MEMCACHED=3.0.3 \  
PHP_DS=1.2.3 \  
PHP_XDEBUG=2_5_5  
  
################################################################################  
# Build instructions  
################################################################################  
  
# Install packages  
RUN \  
set -ex; \  
# echo 'http://alpine.gliderlabs.com/alpine/edge/testing' >
/etc/apk/repositories; \  
# echo "http://alpine.gliderlabs.com/alpine/edge/main" >>
/etc/apk/repositories; \  
# echo "http://alpine.gliderlabs.com/alpine/edge/community" >>
/etc/apk/repositories; \  
sed -i -e 's/v3\\.4/edge/g' /etc/apk/repositories; \  
apk add --no-cache --virtual .run-deps \  
libressl \  
libevent \  
rabbitmq-c \  
bash \  
libmcrypt \  
libmemcached \  
zlib \  
curl; \  
  
apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
rabbitmq-c-dev \  
coreutils \  
libevent-dev \  
zlib-dev \  
libmemcached-dev \  
libmcrypt-dev \  
cyrus-sasl-dev \  
libltdl; \  
  
cd /tmp; \  
curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/${PHP_REDIS}.tar.gz; \  
tar xfz ./redis.tar.gz; \  
mkdir -p /usr/src/php/ext/redis; \  
mv phpredis-${PHP_REDIS}/* /usr/src/php/ext/redis; \  
  
curl -L -o /tmp/amqp.tar.gz https://github.com/pdezwart/php-
amqp/archive/v${PHP_AMQP}.tar.gz; \  
tar xfz /tmp/amqp.tar.gz; \  
mkdir -p /usr/src/php/ext/amqp; \  
mv php-amqp-${PHP_AMQP}/* /usr/src/php/ext/amqp; \  
  
curl -L -o /tmp/apcu.tar.gz
https://github.com/krakjoe/apcu/archive/v${PHP_ACPU}.tar.gz; \  
tar xfz /tmp/apcu.tar.gz; \  
mkdir -p /usr/src/php/ext/apcu; \  
mv apcu-${PHP_ACPU}/* /usr/src/php/ext/apcu; \  
  
curl -L -o /tmp/event.tar.gz https://pecl.php.net/get/event-${PHP_EVENT}.tgz;
\  
tar xfz /tmp/event.tar.gz; \  
mkdir -p /usr/src/php/ext/event; \  
mv event-${PHP_EVENT}/* /usr/src/php/ext/event; \  
  
curl -L -o /tmp/igbinary.tar.gz
https://github.com/igbinary/igbinary/archive/${PHP_IGBINARY}.tar.gz; \  
tar xfz /tmp/igbinary.tar.gz; \  
mkdir -p /usr/src/php/ext/igbinary; \  
mv igbinary-${PHP_IGBINARY}/* /usr/src/php/ext/igbinary; \  
  
curl -L -o /tmp/memcached.tar.gz https://github.com/php-memcached-dev/php-
memcached/archive/v${PHP_MEMCACHED}.tar.gz; \  
tar xfz ./memcached.tar.gz; \  
mkdir -p /usr/src/php/ext/memcached; \  
mv php-memcached-${PHP_MEMCACHED}/* /usr/src/php/ext/memcached; \  
  
  
curl -L -o /tmp/extension.tar.gz https://github.com/php-
ds/extension/archive/v${PHP_DS}.tar.gz; \  
tar xfz ./extension.tar.gz; \  
mkdir -p /usr/src/php/ext/extension; \  
mv extension-${PHP_DS}/* /usr/src/php/ext/extension; \  
  
curl -L -o /tmp/xdebug.tar.gz
https://github.com/xdebug/xdebug/archive/XDEBUG_${PHP_XDEBUG}.tar.gz; \  
tar xfz ./xdebug.tar.gz; \  
mkdir -p /usr/src/php/ext/xdebug; \  
mv xdebug-XDEBUG_${PHP_XDEBUG}/* /usr/src/php/ext/xdebug; \  
  
#Build  
docker-php-ext-install \  
mbstring \  
mysqli \  
igbinary \  
apcu \  
amqp \  
pdo_mysql \  
bcmath \  
opcache \  
sockets \  
memcached \  
extension \  
mcrypt \  
xdebug; \  
  
docker-php-ext-configure event --with-event-core --with-event-extra; \  
docker-php-ext-configure redis --enable-redis-igbinary; \  
docker-php-ext-install event redis; \  
mv /usr/local/etc/php/conf.d/docker-php-ext-event.ini
/usr/local/etc/php/conf.d/z-docker-php-ext-event.ini; \  
  
#Clean up  
apk del .build-deps; \  
rm -Rf \  
/usr/src/php/ext/xdebug \  
/usr/src/php/ext/igbinary \  
/usr/src/php/ext/event \  
/usr/src/php/ext/apcu \  
/usr/src/php/ext/amqp \  
/usr/src/php/ext/redis \  
/usr/src/php/ext/extension \  
/tmp/* \  
/var/tmp/* \  
/var/lib/apt/lists/* \  
/var/cache/apk/*; \  
  
echo $'\n\  
opcache.enable_cli=0 \n\  
opcache.max_accelerated_files=7963 \n\  
opcache.memory_consumption=192 \n\  
opcache.interned_strings_buffer=16 \n\  
opcache.fast_shutdown=1\n'\  
>> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini; \  
  
echo $'\n\  
xdebug.default_enable=${XDEBUG_ENABLE} \n\  
xdebug.idekey=PHPSTORM \n\  
xdebug.remote_handler=dbgp \n\  
xdebug.remote_port=${XDEBUG_PORT} \n\  
xdebug.autostart=${XDEBUG_ENABLE} \n\  
xdebug.remote_autostart=${XDEBUG_ENABLE} \n\  
xdebug.remote_connect_back=1 \n\  
xdebug.remote_enable=${XDEBUG_ENABLE} \n' \  
>> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini;

