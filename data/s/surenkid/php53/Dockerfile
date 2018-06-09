FROM debian:jessie  
MAINTAINER https://github.com/surenkid/  
  
# persistent / runtime deps  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
librecode0 \  
libmysqlclient-dev \  
libsqlite3-0 \  
libxml2 \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# phpize deps  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
ENV GPG_KEYS 0B96609E270F565C13292B24C13C70B87267B52D
0A95E9A026542D53835E3F3A7DEC4E69FC9C83D7 0E604491  
RUN set -xe \  
&& for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
# compile openssl, otherwise --with-openssl won't work  
RUN OPENSSL_VERSION="1.0.2k" \  
&& cd /tmp \  
&& mkdir openssl \  
&& curl -sL "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz"
-o openssl.tar.gz \  
&& curl -sL
"https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz.asc" -o
openssl.tar.gz.asc \  
&& gpg --verify openssl.tar.gz.asc \  
&& tar -xzf openssl.tar.gz -C openssl --strip-components=1 \  
&& cd /tmp/openssl \  
&& ./config && make && make install \  
&& rm -rf /tmp/*  
  
# compile freetds for mssql  
RUN cd /tmp \  
&& curl -sL
"ftp://ftp.gnome.org/mirror/ubuntu/pool/main/f/freetds/freetds_0.91.orig.tar.gz"
-o freetds.tar.gz \  
&& tar -xof freetds.tar.gz \  
&& rm freetds.tar.gz* \  
&& cd freetds-0.91 \  
&& ./configure --prefix=/usr/local/freetds --with-tdsver=7.1 --enable-msdblib
--enable-dbmfix --with-gnu-ld --enable-shared --enable-static \  
&& make && make install \  
&& make clean \  
&& rm -rf /tmp/*  
  
ENV PHP_VERSION 5.3.29  
# php 5.3 needs older autoconf  
# --enable-mysqlnd is included below because it's harder to compile after the
fact the extensions are (since it's a plugin for several extensions, not an
extension in itself)  
RUN buildDeps=" \  
autoconf2.13 \  
libcurl4-openssl-dev \  
libreadline6-dev \  
librecode-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
" \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.xz/from/this/mirror" -o
php.tar.xz \  
&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.xz.asc/from/this/mirror"
-o php.tar.xz.asc \  
&& gpg --verify php.tar.xz.asc \  
&& mkdir -p /usr/src/php \  
&& tar -xof php.tar.xz -C /usr/src/php --strip-components=1 \  
&& rm php.tar.xz* \  
&& cd /usr/src/php \  
&& ./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--enable-fpm \  
\--with-fpm-user=www-data \  
\--with-fpm-group=www-data \  
\--disable-cgi \  
\--enable-mysqlnd \  
\--with-mysql \  
\--with-curl \  
\--with-openssl=/usr/local/ssl \  
\--with-readline \  
\--with-recode \  
\--with-zlib \  
&& make -j"$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& make clean  
  
COPY docker-php-* /usr/local/bin/  
  
# download phpredis to php ext folder  
RUN cd /tmp \  
&& mkdir -p /usr/src/php/ext/phpredis \  
&& curl -sL "https://github.com/phpredis/phpredis/archive/master.tar.gz" -o
phpredis.tar.gz \  
&& tar -xof phpredis.tar.gz -C /usr/src/php/ext/phpredis --strip-components=1
\  
&& rm -rf /tmp/*  
  
# download xdebug to php ext folder  
RUN cd /tmp \  
&& mkdir -p /usr/src/php/ext/xdebug \  
&& curl -sL "https://xdebug.org/files/xdebug-2.2.7.tgz" -o xdebug.tgz \  
&& tar -xof xdebug.tgz -C /usr/src/php/ext/xdebug --strip-components=1 \  
&& rm -rf /tmp/*  
  
# download yaf to php ext folder  
RUN cd /tmp \  
&& mkdir -p /usr/src/php/ext/yaf \  
&& curl -sL "https://github.com/laruence/yaf/archive/yaf-2.3.5.tar.gz" -o
yaf.tar.gz \  
&& tar -xof yaf.tar.gz -C /usr/src/php/ext/yaf --strip-components=1 \  
&& rm -rf /tmp/*  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Fix php 5.3 can't found freetype.h error, fix docker-php-ext-install script
exec error  
RUN mkdir /usr/include/freetype2/freetype \  
&& ln -s /usr/include/freetype2/freetype.h
/usr/include/freetype2/freetype/freetype.h \  
&& chmod +x /usr/local/bin/docker-php-*  
  
# install php extension  
RUN docker-php-ext-install iconv mbstring mcrypt mysqli phpredis yaf xdebug \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure mssql --with-mssql=/usr/local/freetds \  
&& docker-php-ext-install mssql  
  
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
echo '; Ensure worker stdout and stderr are sent to the main error log.'; \  
echo 'catch_workers_output = yes'; \  
} | tee php-fpm.d/docker.conf \  
&& { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = 9000'; \  
} | tee php-fpm.d/zz-docker.conf  
  
# fix php-fpm listen address  
RUN sed -i -e "s/listen = 127.0.0.1:9000/listen = 0.0.0.0:9000/g"
/usr/local/etc/php-fpm.d/www.conf  
  
# fix xdebug library path  
RUN echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20090626/xdebug.so' | tee /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini  
  
# set yaf to name space mode  
RUN echo 'yaf.use_namespace = 1' | tee -a /usr/local/etc/php/conf.d/docker-
php-ext-yaf.ini  
  
EXPOSE 9000  
CMD ["php-fpm"]  

