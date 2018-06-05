FROM composer:1 AS composer  
  
FROM php:7.2-fpm-alpine  
  
ENV PHP_TIMEZONE="UTC" \  
FPM_PHP_USER="www-data" \  
FPM_PHP_GROUP="www-data" \  
FPM_PROCESS_MANAGER="dynamic" \  
FPM_MAX_CHILDREN=5 \  
FPM_START_SERVERS=2 \  
FPM_MIN_SPARE_SERVERS=1 \  
FPM_MAX_SPARE_SERVERS=3 \  
FPM_PROCESS_IDLE_TIMEOUT="10s" \  
COMPOSER_ALLOW_SUPERUSER=1  
RUN set -xe && \  
apk add --no-cache --quiet --virtual .build-deps zlib-dev freetype-dev libpng-
dev libjpeg-turbo-dev icu-dev $PHPIZE_DEPS && \  
sed -i 's#set -x#set +x#' /usr/local/bin/docker-php-ext-configure && \  
docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(getconf _NPROCESSORS_ONLN) && \  
docker-php-ext-install -j${NPROC} zip iconv pdo pdo_mysql gd opcache mbstring
bcmath intl pcntl && \  
sed -i 's#set +x#set -x#' /usr/local/bin/docker-php-ext-configure && \  
pecl install apcu && \  
echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini && \  
runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
apk add --no-cache --virtual .run-deps $runDeps && \  
apk del --quiet .build-deps && \  
true  
  
COPY \--from=composer /usr/bin/composer /usr/bin/composer  
  
ENV DOCKERIZE_VERSION "0.5.0"  
RUN set -xe && \  
curl -sSL \  
https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz | \  
tar -C /usr/local/bin -xzv && \  
true  
  
ENV DUMB_INIT_VERSION "1.2.0"  
RUN set -xe && \  
curl -sSLo /usr/local/bin/dumb-init \  
https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 && \  
chmod +x /usr/local/bin/dumb-init && \  
true  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
CMD ["php-fpm"]  
  
COPY config /usr/local/etc/php/conf.d  
COPY www.conf /usr/local/etc/php-fpm.d/www.conf  

