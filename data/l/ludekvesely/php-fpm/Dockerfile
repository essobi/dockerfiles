FROM alpine:3.3  
MAINTAINER Ludek Vesely <ludek.vesely@email.com>  
  
ENV PHP_VERSION 7.0.5  
  
RUN buildDeps=" build-base re2c file autoconf binutils bison libxml2-dev \  
curl-dev openssl-dev libmcrypt-dev gmp-dev icu-dev wget make git" \  
  
# apk add  
&& apk --update add grep curl zlib tar libxml2 openssl libmcrypt icu
$buildDeps \  
  
# download unpack php-src  
&& mkdir /tmp/php && cd /tmp/php \  
&& wget https://github.com/php/php-src/archive/php-${PHP_VERSION}.tar.gz --no-
verbose \  
&& tar xzf php-${PHP_VERSION}.tar.gz \  
&& cd php-src-php-${PHP_VERSION} \  
  
# compile  
&& ./buildconf --force \  
&& ./configure \  
--prefix=/usr \  
--sysconfdir=/etc/php \  
--with-config-file-path=/etc/php \  
--with-config-file-scan-dir=/etc/php/conf.d \  
--enable-fpm --with-fpm-user=root --with-fpm-group=root \  
--enable-mbstring \  
--enable-zip \  
--enable-bcmath \  
--enable-opcache \  
--enable-pcntl \  
--enable-mysqlnd \  
--enable-sockets \  
--enable-soap \  
--enable-calendar \  
--enable-intl \  
--enable-json \  
--enable-dom \  
--enable-libxml --with-libxml-dir=/usr \  
--enable-xml \  
--enable-xmlreader \  
--enable-session \  
--enable-sysvmsg \  
--enable-sysvsem \  
--enable-sysvshm \  
--disable-cgi \  
--disable-debug \  
--disable-rpath \  
--disable-static \  
--disable-phpdbg \  
--with-libdir=/lib/x86_64-linux-gnu \  
--with-curl \  
--with-mcrypt \  
--with-iconv \  
--with-zlib --with-zlib-dir=/usr \  
--with-openssl \  
--with-mhash \  
--with-pcre-regex \  
--with-pdo-mysql \  
--with-mysqli \  
--with-xmlrpc \  
--with-pear \  
&& make \  
&& make install \  
&& make clean \  
  
# strip debug symbols from the binary (GREATLY reduces binary size)  
&& strip -s /usr/bin/php \  
  
# phpredis is not on PECL  
&& cd /tmp \  
&& git clone https://github.com/phpredis/phpredis.git \  
&& cd phpredis \  
&& git checkout php7 \  
&& phpize && ./configure && make && make install \  
  
# remove PHP dev dependencies  
&& apk del $buildDeps \  
  
# other clean up  
&& cd / \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
COPY php /etc/php  
  
EXPOSE 9000  
  
CMD ["php-fpm", "--allow-to-run-as-root", "--fpm-config", "/etc/php/php-
fpm.conf", "-c", "/etc/php/php.ini"]  
  

