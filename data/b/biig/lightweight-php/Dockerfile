FROM alpine:edge  
MAINTAINER Manu <manuel.barraud@biig.fr>  
ENV PHP_VERSION php-7.1.7  
RUN apk add \--update curl tar xz libedit libxml2 libjpeg-turbo libwebp cyrus-
sasl icu-libs libpng cyrus-sasl libmemcached && \  
apk add \--update \--virtual build-deps build-base git make autoconf file
pkgconf re2c binutils bison \  
curl-dev libedit-dev libxml2-dev libressl-dev wget ca-certificates libwebp-dev
libjpeg-turbo-dev libpng-dev icu-dev libmemcached-dev cyrus-sasl-dev && \  
update-ca-certificates && \  
cd / && \  
git clone https://github.com/php/php-src.git && \  
cd /php-src && git checkout tags/$PHP_VERSION && cd / && \  
cd /php-src && ./buildconf \--force && \  
./configure -prefix=/usr \--sysconfdir=/etc \--with-config-file-
path="/etc/php" \--with-config-file-scan-dir="/etc/php/conf.d" \--disable-cgi
\--with-curl \--with-libedit \--with-openssl=/usr \--with-zlib \--with-iconv
\--with-gd \--with-jpeg-dir=/usr \--with-webp-dir=/usr \--enable-bcmath
\--enable-zip \--enable-mbstring \--enable-intl \--enable-pcntl \--enable-ftp
\--enable-exif \--enable-calendar \--enable-sysvmsg \--enable-sysvsem
\--enable-sysvshm \--disable-phpdbg && \  
make -j8 && make install-binaries install-pear install-pharcmd install-modules
install-build install-programs install-headers && \  
mkdir -p /etc/php/ && \  
cp php.ini-production /etc/php/php.ini && \  
pecl config-set php_ini /etc/php/php.ini && \  
pear config-set php_ini /etc/php/php.ini && \  
pecl install memcached redis && \  
strip \--strip-all /usr/bin/php && \  
cd / && rm -r php-src && rm -r /usr/include && rm -r /usr/php && rm -r
/usr/lib/php/build && \  
rm /usr/lib/php/extensions/no-debug-non-zts-20160303/opcache.a && \  
apk del build-deps && rm -rf /var/cache/apk/* && rm -rf /tmp/*  

