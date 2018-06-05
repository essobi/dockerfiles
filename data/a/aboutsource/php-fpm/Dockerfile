FROM debian:jessie  
  
MAINTAINER support@aboutsource.net  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
libxml2 \  
autoconf \  
gcc \  
g++ \  
libc-dev \  
make \  
pkg-config \  
file \  
bison \  
re2c \  
bzip2 \  
gobjc++ \  
libicu-dev \  
libfcgi-dev \  
libssl-dev \  
libbz2-dev \  
libmcrypt-dev \  
libxml2-dev \  
libjpeg-dev \  
libpng-dev \  
libfreetype6-dev \  
libreadline6-dev \  
imagemagick \  
libmagickwand-dev \  
libmagic-dev \  
libcurl4-openssl-dev && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
RUN gpg \  
\--keyserver pool.sks-keyservers.net \  
\--recv-keys 6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3
0BD78B5F97500D450838F95DFE857D9A90D90EC1  
  
RUN curl -SL "http://php.net/get/php-5.6.33.tar.bz2/from/this/mirror" -o
php.tar.bz2 && \  
curl -sL "http://php.net/get/php-5.6.33.tar.bz2.asc/from/this/mirror" -o
php.tar.bz2.asc && \  
gpg --verify php.tar.bz2.asc && \  
mkdir -p /usr/src/php && \  
tar -xf php.tar.bz2 -C /usr/src/php --strip-components=1 && \  
rm php.tar.bz2* && \  
cd /usr/src/php && \  
./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--enable-fpm \  
\--with-fpm-user=www-data \  
\--with-fpm-group=www-data \  
\--enable-mbstring \  
\--with-libxml-dir=/usr \  
\--with-curl \  
\--with-mcrypt \  
\--with-gd \  
\--disable-rpath \  
\--enable-inline-optimization \  
\--with-bz2 \  
\--enable-sockets \  
\--enable-sysvsem \  
\--enable-sysvshm \  
\--enable-pcntl \  
\--enable-mbregex \  
\--with-mhash \  
\--enable-zip \  
\--with-pcre-regex \  
\--with-mysql \  
\--with-pdo-mysql \  
\--with-mysqli \  
\--with-jpeg-dir=/usr \  
\--with-png-dir=/usr \  
\--enable-gd-native-ttf \  
\--with-openssl=/usr \  
\--with-libdir=lib64 \  
\--with-libxml-dir=/usr \  
\--enable-exif \  
\--with-gettext \  
\--enable-shmop \  
\--enable-sysvmsg \  
\--enable-bcmath \  
\--enable-ftp \  
\--enable-intl \  
\--disable-cgi \  
\--with-readline \  
\--with-zlib \  
\--with-libdir=/lib/x86_64-linux-gnu && \  
make -j"$(nproc)" && \  
make install && \  
make clean  
  
RUN pecl install imagick  
  
RUN cp /usr/src/php/php.ini-development "$PHP_INI_DIR/php.ini"  
RUN echo "extension=imagick.so" > "$PHP_INI_DIR/conf.d/extensions.ini"  
  
WORKDIR /var/www/html  
COPY php-fpm.conf /usr/local/etc/  
  
EXPOSE 9000  
  
CMD ["php-fpm"]  

