FROM php:7.1-fpm-alpine  
  
MAINTAINER Pavel Bezrukov <bezrukov.ps@gmail.com>  
  
ENV TERM xterm  
  
ENV JPEGOPTIM_VERSION=1.4.4  
ENV OPTIPNG_VERSION=0.7.6  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
  
RUN apk add --no-cache --virtual .persistent-deps \  
mc \  
icu-dev \  
libmcrypt-dev \  
libxml2-dev \  
zeromq \  
git \  
libmemcached \  
curl \  
libcurl \  
ssmtp \  
freetype-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
imagemagick-dev \  
pcre-dev \  
&& apk add --no-cache --virtual .build-deps \  
autoconf \  
cmake \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
git \  
pkgconf \  
re2c \  
openssl-dev \  
zeromq-dev \  
libmemcached-dev \  
cyrus-sasl-dev \  
openssl-dev \  
curl-dev \  
libtool \  
&& docker-php-source extract \  
&& docker-php-ext-configure intl --enable-intl \  
&& docker-php-ext-configure pcntl --enable-pcntl \  
&& docker-php-ext-configure mbstring --enable-mbstring \  
&& docker-php-ext-configure soap --enable-soap \  
&& docker-php-ext-install \  
intl \  
mcrypt \  
pcntl \  
mbstring \  
mysqli \  
soap \  
zip \  
# memcached  
&& git clone --branch php7 https://github.com/php-memcached-dev/php-memcached/
/usr/src/php/ext/memcached/ \  
&& docker-php-ext-configure memcached --disable-memcached-sasl \  
&& docker-php-ext-install memcached \  
# memcache  
&& git clone --branch php7 https://github.com/websupport-sk/pecl-memcache/
/usr/src/php/ext/memcache/ \  
&& docker-php-ext-configure memcache \  
&& docker-php-ext-install memcache \  
&& docker-php-ext-configure curl \  
&& docker-php-ext-install curl \  
&& docker-php-ext-configure opcache --enable-opcache \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install iconv \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
  
  
#####################################  
# Image compression:  
#####################################  
#jpegoptim  
RUN apk add --no-cache --virtual .build-dependencies-jpegoptim libjpeg-turbo-
dev \  
&& mkdir /usr/src/jpegoptim \  
&& cd /usr/src/jpegoptim \  
&& git clone -b RELEASE.${JPEGOPTIM_VERSION}
https://github.com/tjko/jpegoptim.git . \  
&& ./configure --prefix=/usr && make && make strip && make install \  
&& cd / \  
&& apk del .build-dependencies-jpegoptim \  
&& rm -rf /usr/src/jpegoptim  
  
#optipng  
RUN mkdir -p /usr/src/optipng \  
&& wget -O -
http://downloads.sourceforge.net/project/optipng/OptiPNG/optipng-${OPTIPNG_VERSION}/optipng-${OPTIPNG_VERSION}.tar.gz
| tar xz -C /usr/src/optipng --strip-components=1 \  
&& cd /usr/src/optipng \  
&& ./configure --prefix=/usr && make && make install \  
&& cd / \  
&& rm -rf /usr/src/optipng  
  
  
#####################################  
# Set ssmtp  
#####################################  
  
ADD ./ssmtp/ /etc/ssmtp/  
  
  
#  
#--------------------------------------------------------------------------  
# Final Touch  
#--------------------------------------------------------------------------  
#  
# Clean up  
RUN rm -rf /tmp/* /var/cache/apk/*  

