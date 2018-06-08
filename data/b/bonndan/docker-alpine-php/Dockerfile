FROM alpine:3.3  
  
# define PHP and libiconv version  
ENV PHP_VERSION 7.0.2  
ENV LIBICONV_VERSION 1.14  
  
# define workdir to home  
WORKDIR /install  
  
# install build tools  
RUN apk add -U grep build-base tar re2c make file \  
  
# PHP dependencies  
libxml2-dev curl-dev \  
openssl-dev libjpeg-turbo-dev libpng-dev libmcrypt-dev icu-dev && \  
  
# download sources  
curl -SL http://cz1.php.net/get/php-${PHP_VERSION}.tar.gz/from/this/mirror |
tar -xz -C ~/ && \  
mv ~/php-${PHP_VERSION} ~/php && \  
  
# install php from source  
~/php/configure --prefix=/usr \  
--with-layout=GNU \  
--enable-inline-optimization \  
--disable-phpdbg \  
--enable-cli \  
--disable-cgi \  
--enable-fpm \  
--enable-mbstring \  
--enable-zip \  
--with-curl \  
--with-mcrypt \  
--with-iconv \  
--with-gd \  
--with-mysqli \  
--with-pdo-mysql \  
--enable-opcache \  
--with-jpeg-dir=/usr \  
--with-png-dir=/usr \  
--with-zlib-dir=/usr \  
--with-openssl \  
--with-zlib=/usr \  
--enable-intl \  
--disable-debug \  
--disable-rpath \  
--disable-static \  
--disable-pcntl \  
--enable-shared \  
--with-config-file-path=/etc/php \  
--with-config-file-scan-dir=/etc/php/conf.d \  
--sysconfdir=/etc/php \  
--without-pear \  
--enable-sockets \  
&& \  
  
make && make install && \  
  
# add non-dev PHP dependencies to APK  
apk add -u libxml2 curl \  
openssl libjpeg-turbo libpng libmcrypt \  
icu && \  
  
# remove dev PHP dependencies  
apk del grep build-base tar re2c make file \  
libxml2-dev curl-dev \  
openssl-dev libjpeg-turbo-dev libpng-dev libmcrypt-dev \  
icu-dev && \  
  
# clear apk cache  
rm -rf /var/cache/apk/* && \  
  
# remove sources  
rm -rf ~/php ~/libiconv && rm -rf /install  
  
WORKDIR /  
  
# replace origin iconv  
ENV LD_PRELOAD /usr/local/lib/preloadable_libiconv.so  
  
# copy default PHP config  
COPY /php.ini /etc/php/php.ini  

