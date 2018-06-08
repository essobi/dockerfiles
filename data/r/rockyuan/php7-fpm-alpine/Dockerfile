FROM php:7.2.6-fpm-alpine3.7  
# 第三方插件的版本号  
ENV RABBITMQ_VERSION v0.9.0  
ENV PHP_AMQP_VERSION v1.9.3  
ENV PHP_REDIS_VERSION 4.0.2  
ENV PHP_MONGO_VERSION 1.4.3  
ENV PHP_MEMCACHED_VERSION v3.0.4  
ENV PHP_IMAGICK_VERSION 3.4.3  
ENV PHP_SWOOLE_VERSION v2.2.0  
ENV PHP_XDEBUG_VERSION 2.6.0  
  
ENV PHPIZE_DEPS \  
autoconf \  
cmake \  
file \  
g++ \  
gcc \  
libc-dev \  
pcre-dev \  
make \  
git \  
pkgconf \  
re2c  
  
# 安装需要的插件  
RUN set -ex; \  
\  
apk add \--no-cache \--virtual .build-deps \  
${PHPIZE_DEPS} \  
# for gd extension  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
# for intl extension  
icu-dev \  
# for memcached  
libmemcached-dev \  
zlib-dev \  
cyrus-sasl-dev \  
# for swoole  
linux-headers \  
# for mcrypt extension DEPRECATED since PHP 7.1  
#libmcrypt-dev \  
# for ...  
openssl-dev \  
libtool \  
tzdata; \  
\  
apk add imagemagick-dev \--update-cache \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/main \--allow-untrusted; \  
\  
docker-php-ext-configure gd \--with-freetype-dir=/usr \--with-png-dir=/usr
\--with-jpeg-dir=/usr; \  
docker-php-ext-configure pdo_mysql \--with-pdo-mysql; \  
docker-php-ext-configure bcmath \--enable-bcmath; \  
docker-php-ext-configure intl \--enable-intl; \  
docker-php-ext-install gd pdo_mysql mysqli zip bcmath intl opcache sockets
iconv; \  
\  
runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive
/usr/local/lib/php/extensions \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)"; \  
apk add \--virtual .phpexts-rundeps $runDeps libmemcached-libs libssl1.0
imagemagick vim; \  
\  
git clone \--branch ${PHP_IMAGICK_VERSION}
https://github.com/mkoppanen/imagick.git /tmp/php-imagick; \  
docker-php-ext-configure /tmp/php-imagick; \  
docker-php-ext-install /tmp/php-imagick; \  
\  
pecl install apcu; \  
docker-php-ext-enable apcu; \  
\  
git clone \--branch ${RABBITMQ_VERSION}
https://github.com/alanxz/rabbitmq-c.git /tmp/rabbitmq; \  
cd /tmp/rabbitmq; \  
mkdir build; \  
cd build; \  
cmake ..; \  
cmake \--build . \--target install; \  
cp -r /usr/local/lib64/* /usr/lib/; \  
\  
git clone \--branch ${PHP_AMQP_VERSION} https://github.com/pdezwart/php-
amqp.git /tmp/php-amqp; \  
cd /tmp/php-amqp; \  
phpize; \  
./configure; \  
make; \  
make install; \  
#make test; \  
\  
git clone \--branch ${PHP_REDIS_VERSION} https://github.com/phpredis/phpredis
/tmp/phpredis; \  
cd /tmp/phpredis; \  
phpize; \  
./configure; \  
make; \  
make install; \  
make test; \  
\  
git clone \--branch ${PHP_MONGO_VERSION} https://github.com/mongodb/mongo-php-
driver /tmp/php-mongo; \  
cd /tmp/php-mongo; \  
git submodule sync; \  
git submodule update \--init; \  
phpize; \  
./configure; \  
make; \  
make install; \  
make test; \  
\  
git clone \--branch ${PHP_MEMCACHED_VERSION} https://github.com/php-memcached-
dev/php-memcached.git /tmp/php-memcached; \  
docker-php-ext-configure /tmp/php-memcached; \  
docker-php-ext-install /tmp/php-memcached; \  
\  
# 安装swoole  
git clone \--branch ${PHP_SWOOLE_VERSION} https://github.com/swoole/swoole-
src.git /tmp/php-swoole; \  
docker-php-ext-configure /tmp/php-swoole; \  
docker-php-ext-install /tmp/php-swoole; \  
\  
# 开发环境启用xdebug  
git clone \--branch ${PHP_XDEBUG_VERSION} https://github.com/xdebug/xdebug.git
/tmp/php-xdebug; \  
docker-php-ext-configure /tmp/php-xdebug; \  
docker-php-ext-install /tmp/php-xdebug; \  
\  
# 系统时间  
cp /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime; \  
echo "Asia/Hong_Kong" > /etc/timezone; \  
\  
apk del .build-deps; \  
rm -rf /tmp/*; \  
# 建立默认工作目录  
mkdir -p /data  
# iconv运行库  
RUN apk add gnu-libiconv \--update-cache \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ \--allow-untrusted  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
  
# Copy configuration  
COPY config/php.ini $PHP_INI_DIR  
COPY config/amqp.ini $PHP_INI_DIR/conf.d/  
COPY config/redis.ini $PHP_INI_DIR/conf.d/  
COPY config/mongodb.ini $PHP_INI_DIR/conf.d/  
# 根据系统环境变量修改命令行提示  
COPY config/env_prompt.sh /etc/profile.d/env_prompt.sh  
ENV ENV="/etc/profile"  
# install composer  
RUN curl \--tlsv1 -sS https://getcomposer.org/installer | php --
\--filename=composer \--install-dir=/bin  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
WORKDIR /data  

