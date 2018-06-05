FROM php:7.0-fpm-alpine  
  
MAINTAINER Andre Schuurman <docker@drsdre.org>  
  
LABEL Description="This image is PHP FPM 7.0 running on Alpine with extension
needed for Yii2 applications" Vendor="Andre Schuurman" Version="7.0-cli-
alpine"  
# Install dependencies  
RUN apk --no-cache --update add \  
libxml2-dev \  
sqlite-dev \  
curl-dev \  
gettext-dev \  
icu-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
freetype-dev \  
libxslt-dev  
  
# Configure PHP extensions  
RUN docker-php-ext-configure bcmath && \  
docker-php-ext-configure curl && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-configure gettext && \  
docker-php-ext-configure iconv && \  
docker-php-ext-configure intl && \  
docker-php-ext-configure json && \  
docker-php-ext-configure mbstring && \  
docker-php-ext-configure mcrypt && \  
docker-php-ext-configure pcntl && \  
docker-php-ext-configure pdo && \  
docker-php-ext-configure pdo_mysql && \  
docker-php-ext-configure simplexml && \  
docker-php-ext-configure xml && \  
docker-php-ext-configure xsl  
  
# Build and install PHP extensions  
RUN docker-php-ext-install \  
bcmath \  
curl \  
gd \  
gettext \  
iconv \  
intl \  
json \  
mbstring \  
mcrypt \  
pcntl \  
pdo \  
pdo_mysql \  
simplexml \  
xml \  
xsl  
  
# Install PHP PECL extensions  
RUN apk add --no-cache \  
$PHPIZE_DEPS \  
&& pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable redis  
  
# Change memory limit  
RUN echo 'memory_limit = 2G ' >> /usr/local/etc/php/php.ini  
  
# Cleanup  
RUN rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*

