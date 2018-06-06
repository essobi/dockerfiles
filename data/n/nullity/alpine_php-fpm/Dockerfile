FROM alpine:latest  
  
MAINTAINER nullity  
  
# persistent / runtime deps  
ENV PHPIZE_DEPS \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c  
RUN apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
curl \  
tar \  
xz  
  
# ensure www-data user exists  
RUN set -x \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data  
# 82 is the standard uid/gid for "www-data" in Alpine  
  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=www-data --with-fpm-
group=www-data  
  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
curl-dev \  
libedit-dev \  
libxml2-dev \  
libressl-dev \  
sqlite-dev \  
libmcrypt-dev \  
freetype-dev \  
postgresql-dev \  
libpng-dev \  
jpeg-dev \  
bzip2-dev \  
openjpeg-dev \  
gmp-dev \  
libc-dev \  
libxslt-dev \  
gettext-dev \  
wget \  
&& mkdir -p /usr/src \  
&& cd /usr/src/ \  
&& wget php.net$(curl http://php.net/downloads.php|grep -o '<a
href="/get/php-7[^"]*"'|head -1|sed 's/[^\/]*//'|sed 's/.$//'|sed
's/a\//this\//') -O-|tar xfj - \  
&& cd /usr/src/php-7* \  
&& ./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
$PHP_EXTRA_CONFIGURE_ARGS \  
\--disable-cgi \  
# --enable-mysqlnd is included here because it's harder to compile after the
fact than extensions are (since it's a plugin for several extensions, not an
extension in itself)  
\--enable-mysqlnd \  
# --enable-mbstring is included here because otherwise there's no way to get
pecl to use it properly (see https://github.com/docker-library/php/issues/195)  
\--enable-mbstring \  
\--enable-sockets \  
\--enable-pcntl \  
\--enable-mbregex \  
\--enable-bcmath \  
\--enable-zip \  
\--enable-inline-optimization \  
\--enable-gd-native-ttf \  
\--enable-ftp \  
\--enable-opcache \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
\--with-bz2 \  
\--with-pgsql \  
\--with-gmp \  
\--with-pdo-pgsql \  
\--with-libxml \  
\--with-mcrypt \  
\--with-gd \  
\--with-mhash \  
\--with-xsl \  
\--with-gettext \  
\--with-pcre-regex \  
\--with-pdo-mysql \  
\--with-mysqli \  
&& make \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip
--strip-all '{}' + || true; } \  
&& make clean \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .php-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/php-7*  
  
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
  
EXPOSE 9000  
CMD ["php-fpm"]  

