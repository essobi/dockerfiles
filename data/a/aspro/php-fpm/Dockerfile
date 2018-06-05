ARG PHP_VER=7.2  
ARG ALPINE_VERSION=3.7  
  
FROM php:${PHP_VER}-fpm-alpine${ALPINE_VERSION}  
  
RUN set -xe \  
# php build-dependencies  
&& apk --update add --virtual .build-deps \  
$PHPIZE_DEPS \  
tzdata \  
libzip-dev \  
icu-dev \  
postgresql-dev \  
  
&& cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime \  
  
&& docker-php-ext-configure zip --with-libzip \  
&& docker-php-ext-configure pcntl --enable-pcntl \  
  
# install php modules  
&& docker-php-ext-install -j$(nproc) \  
pdo_pgsql \  
pdo_mysql \  
pgsql \  
mysqli \  
zip \  
opcache \  
intl \  
pcntl \  
  
&& pecl install \  
xdebug \  
redis \  
apcu \  
&& pecl clear-cache \  
&& docker-php-ext-enable \  
redis \  
apcu \  
opcache \  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive
/usr/local/lib/php/extensions \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .api-phpexts-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer  
  
RUN set -xe \  
&& apk add --no-cache git \  
&& COMPOSER_ALLOW_SUPERUSER=1 \  
composer global require "hirak/prestissimo:^0.3" \  
\--prefer-dist --no-progress \  
\--no-suggest --classmap-authoritative \  
&& composer clear-cache \  
&& addgroup app \  
&& adduser -D -S -s /sbin/nologin -G app app \  
&& sed -i \  
-e "s/;catch_workers_output\s*=\s*[^\n]\+/catch_workers_output = yes/g" \  
-e "s/pm.max_children = [^\n]\+/pm.max_children = \${PHP_PM_MAX_CHILDREN}/g" \  
-e "s/pm.start_servers = [^\n]\+/pm.start_servers = \${PHP_PM_START_SERVERS}/g" \  
-e "s/pm.min_spare_servers = [^\n]\+/pm.min_spare_servers = \${PHP_PM_MIN_SPARE_SERVERS}/g" \  
-e "s/pm.max_spare_servers = [^\n]\+/pm.max_spare_servers = \${PHP_PM_MAX_SPARE_SERVERS}/g" \  
-e "s/;pm.max_requests = [^\n]\+/pm.max_requests = \${PHP_PM_MAX_REQUESTS}/g" \  
-e "s/user = [^\n]\+/user = app/g" \  
-e "s/group = [^\n]\+/group = app/g" \  
-e "s/;listen.mode = [^\n]\+/listen.mode = 0666/g" \  
-e "s/;listen.owner = [^\n]\+/listen.owner = app/g" \  
-e "s/;listen.group = [^\n]\+/listen.group = app/g" \  
-e "s/listen = [^\n]\+/listen = \${PHP_LISTEN}/g" \  
-e "s/^;clear_env = [^\n]\+$/clear_env = no/" \  
/usr/local/etc/php-fpm.d/www.conf  
  
ENV APP_DIR=/app \  
APP_ENV=prod \  
PHP_MEMORY_LIMIT=128M \  
PHP_POST_MAX_SIZE=100M \  
PHP_UPLOAD_MAX_FILESIZE=100M \  
PHP_PM_MAX_CHILDREN=4 \  
PHP_PM_START_SERVERS=3 \  
PHP_PM_MIN_SPARE_SERVERS=2 \  
PHP_PM_MAX_SPARE_SERVERS=4 \  
PHP_PM_MAX_REQUESTS=200 \  
PHP_LISTEN=9000 \  
PHP_DISPLAY_ERRORS=0 \  
PHP_SHORT_OPEN_TAG=Off \  
EXPOSE_PHP=0 \  
PHP_OPCACHE_MEMORY_CONSUMPTION=256 \  
PHP_OPCACHE_MAX_ACCELERATED_FILES=20000 \  
PHP_OPCACHE_VALIDATE_TIMESTAMPS=0 \  
PHP_REALPATH_CACHE_SIZE=4096K \  
PHP_REALPATH_CACHE_TTL=600 \  
COMPOSER_ALLOW_SUPERUSER=1 \  
PATH="${PATH}:/root/.composer/vendor/bin"  
  
ADD rootfs /  
RUN chown -R app:app ${APP_DIR} \  
&& find ${APP_DIR} -type d -exec chmod 755 {} \; \  
&& find ${APP_DIR} -type f -exec chmod 644 {} \; \  
&& find /usr/local/bin -type f -exec chmod +x {} \;  
  
WORKDIR $APP_DIR  
ENTRYPOINT ["docker-entrypoint"]  
CMD ["php-fpm"]

