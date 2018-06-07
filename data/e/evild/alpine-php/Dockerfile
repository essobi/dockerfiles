FROM evild/alpine-base:3.0.0  
MAINTAINER Dominique HAAS <contact@dominique-haas.fr>  
  
  
ARG PHP_INI_DIR=/usr/local/etc/php  
ARG PHP_EXTRA_CONFIGURE_ARGS="--enable-fpm --with-fpm-user=www-data --with-
fpm-group=www-data"  
ARG GPG_KEYS=0BD78B5F97500D450838F95DFE857D9A90D90EC1  
ARG PHP_VERSION=5.5.38  
ARG PHP_FILENAME=php-5.5.38.tar.xz  
ARG
PHP_SHA256=cb527c44b48343c8557fe2446464ff1d4695155a95601083e5d1f175df95580f  
  
  
RUN apk add --no-cache --virtual .phpize-deps \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c \  
&& apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
curl  
  
RUN set -x \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data  
RUN mkdir -p $PHP_INI_DIR/conf.d \  
&& apk add --no-cache --virtual .build-deps \  
curl-dev \  
gnupg \  
libedit-dev \  
libxml2-dev \  
openssl-dev \  
sqlite-dev \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME/from/this/mirror" -o
"$PHP_FILENAME" \  
&& echo "$PHP_SHA256 *$PHP_FILENAME" | sha256sum -c - \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o
"$PHP_FILENAME.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done \  
&& gpg --batch --verify "$PHP_FILENAME.asc" "$PHP_FILENAME" \  
&& rm -r "$GNUPGHOME" "$PHP_FILENAME.asc" \  
&& mkdir -p /usr/src \  
&& tar -Jxf "$PHP_FILENAME" -C /usr/src \  
&& mv "/usr/src/php-$PHP_VERSION" /usr/src/php \  
&& rm "$PHP_FILENAME" \  
&& cd /usr/src/php \  
&& ./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
$PHP_EXTRA_CONFIGURE_ARGS \  
\--disable-cgi \  
\--enable-mysqlnd \  
\--enable-mbstring \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
&& make -j"$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .php-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
WORKDIR /var/www/html  
  
RUN set -ex \  
&& cd /usr/local/etc \  
&& if [ -d php-fpm.d ]; then \  
# for some reason, upstream's php-fpm.conf.default has "include=NONE/etc/php-
fpm.d/*.conf"  
sed 's!=NONE/!=!g' php-fpm.conf.default | tee php-fpm.conf > /dev/null; \  
cp php-fpm.d/www.conf.default php-fpm.d/www.conf; \  
else \  
# PHP 5.x don't use "include=" by default, so we'll create our own simple
config that mimics PHP 7+ for consistency  
mkdir php-fpm.d; \  
cp php-fpm.conf.default php-fpm.d/www.conf; \  
{ \  
echo '[global]'; \  
echo 'include=etc/php-fpm.d/*.conf'; \  
} | tee php-fpm.conf; \  
fi \  
&& { \  
echo '[global]'; \  
echo 'error_log = /proc/self/fd/2'; \  
echo; \  
echo '[www]'; \  
echo '; if we send this to /proc/self/fd/1, it never appears'; \  
echo 'access.log = /proc/self/fd/2'; \  
echo; \  
echo 'clear_env = no'; \  
echo; \  
echo '; Ensure worker stdout and stderr are sent to the main error log.'; \  
echo 'catch_workers_output = yes'; \  
} | tee php-fpm.d/docker.conf \  
&& { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = [::]:9000'; \  
} | tee php-fpm.d/zz-docker.conf  
  
ADD root /  
  
EXPOSE 9000  

