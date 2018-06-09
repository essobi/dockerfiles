# php7  
#  
FROM alpine:edge  
MAINTAINER Tesla <tesla@v-ip.fr>  
ENV PHP_VERSION php-7.2.4  
RUN apk update  
RUN apk add \--update curl tar xz libedit libxml2 && \  
apk add \--update \--virtual build-deps build-base git make autoconf file
pkgconf re2c binutils bison \  
curl-dev libedit-dev libxml2-dev libressl-dev wget ca-certificates && \  
update-ca-certificates && \  
cd / && \  
git clone \--branch $PHP_VERSION \--depth 1 https://github.com/php/php-src.git
&& \  
#cd /php-src && git checkout tags/$PHP_VERSION --depth=1 && cd / && \  
cd /php-src && ./buildconf \--force && ./configure -prefix=/usr
\--sysconfdir=/etc \--with-config-file-path="/etc/php" \--with-config-file-
scan-dir="/etc/php/conf.d" \--disable-cgi \--with-curl \--with-libedit
\--with-openssl=/usr/ \--with-zlib \--enable-fpm \--with-fpm-user=www-data
\--with-fpm-group=www-data \--disable-phpdbg && \  
make -j5 && make install-binaries install-pear install-pharcmd install-modules
&& \  
strip \--strip-all /usr/sbin/php-fpm && \  
strip \--strip-all /usr/bin/php && \  
cd / && rm -r php-src && \  
rm /usr/lib/php/extensions/no-debug-non-zts-20170718/opcache.a && \  
apk del build-deps  
  
RUN deluser xfs && adduser www-data -u 33 -g 33 -D  
EXPOSE 9000  
  
COPY php-fpm.conf /etc/php-fpm.conf  
CMD ["php-fpm","-F"]  
  

