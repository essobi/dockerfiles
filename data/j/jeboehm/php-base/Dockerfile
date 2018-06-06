ARG PHP_VER=7.2  
ARG COMPOSER_VER=1.6.2  
  
FROM composer:${COMPOSER_VER}  
  
FROM php:${PHP_VER}-fpm-alpine  
  
LABEL maintainer="jeff@ressourcenkonflikt.de"  
ENV COMPOSER_ALLOW_SUPERUSER=1  
  
RUN apk add --no-cache \  
ca-certificates \  
curl \  
freetype \  
freetype-dev \  
git \  
icu-dev \  
imagemagick \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
libpng \  
libpng-dev \  
make \  
mysql-client \  
pcre-dev \  
unzip \  
wget && \  
apk add --no-cache --virtual build-deps \  
autoconf \  
automake \  
build-base \  
coreutils \  
imagemagick-dev \  
libtool && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) \  
bcmath \  
gd \  
intl \  
mysqli \  
opcache \  
pdo_mysql \  
zip && \  
pecl install \  
apcu \  
imagick \  
redis \  
xdebug && \  
docker-php-ext-enable \  
apcu \  
imagick \  
redis && \  
rm -rf /tmp/pear && \  
apk del build-deps && \  
update-ca-certificates && \  
ln -s /usr/local/bin/php /usr/bin/php  
  
COPY --from=composer /usr/bin/composer /usr/bin/composer  
COPY rootfs/ /  

