FROM debian:jessie  
  
# phpize deps  
RUN apt-get update && apt-get install -y \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# persistent / runtime deps  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=root --with-fpm-
group=root  
  
ENV GPG_KEYS 1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763  
  
ENV PHP_VERSION 7.0.5  
ENV PHP_FILENAME php-7.0.5.tar.xz  
ENV PHP_SHA256
c41f1a03c24119c0dd9b741cdb67880486e64349fc33527767f6dc28d3803abb  
  
RUN set -xe \  
&& buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libcurl4-openssl-dev \  
libedit-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
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
&& mkdir -p /usr/src/php \  
&& tar -xf "$PHP_FILENAME" -C /usr/src/php --strip-components=1 \  
&& rm "$PHP_FILENAME" \  
&& cd /usr/src/php \  
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
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
&& make -j"$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps  
  
COPY docker-php-ext-* /usr/local/bin/  
  
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
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmysqlclient-dev \  
libxml2-dev \  
libfontconfig \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install mysqli pdo pdo_mysql \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-install soap  
  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.remote_autostart=0" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
COPY config/php.ini /usr/local/etc/php/  
  
CMD ["php-fpm", "-R"]  

