FROM php:7-fpm-alpine  
MAINTAINER snappy.kop@gmail.com (http://snappytux.com)  
  
ENV COMPOSER_VERSION 1.4.2  
ENV BUILD_DEPS build-base \  
autoconf \  
gcc \  
libc-dev \  
file \  
binutils \  
bison \  
readline-dev \  
libxml2-dev \  
curl-dev \  
openssl-dev \  
db-dev \  
enchant-dev \  
expat-dev \  
freetds-dev \  
gdbm-dev \  
gettext-dev \  
libevent-dev \  
libgcrypt-dev \  
libxslt-dev \  
unixodbc-dev \  
zlib-dev \  
krb5-dev \  
libical-dev \  
libxpm-dev \  
build-base  
  
RUN apk add --update ${BUILD_DEPS} \  
libtool \  
gzip \  
patch \  
perl \  
pcre \  
imap \  
imagemagick \  
freetype \  
libpng \  
libjpeg-turbo \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
libc-dev \  
openssl \  
libmcrypt-dev && \  
# Install Composer  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION} && \  
# Install the PHP mcrypt and pdo_mysql extention  
docker-php-ext-install mcrypt pdo_mysql && \  
# Install the PHP gd library  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
docker-php-ext-install -j${NPROC} gd && \  
# Install php mongo driver  
pecl install mongodb && \  
pecl clear-cache && \  
docker-php-ext-enable mongodb && \  
# Cleanup  
apk del --purge ${BUILD_DEPS} && \  
rm -rf /var/cache/apk/* /tmp/* /root/.composer  
  
EXPOSE 9000  

