FROM php:5.6-fpm-alpine  
MAINTAINER Stayfi B. <stayfi@gmail.com>  
  
RUN apk upgrade --update \  
&& apk add --no-cache --virtual .build-deps \  
  
freetype-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
  
sqlite-dev \  
openssl-dev \  
curl-dev \  
libxml2-dev \  
ssmtp \  
icu-dev \  
autoconf \  
g++ \  
make \  
  
&& docker-php-ext-install \  
iconv json mcrypt mbstring mysql mysqli pdo_mysql pdo_sqlite phar curl ftp
hash session simplexml tokenizer xml xmlrpc zip intl pcntl \  
&& docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ \--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
gd \  
  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& sed -i '1 a xdebug.remote_autostart=true' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_connect_back=1 '
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_port=9001' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
  
&& rm -rf /var/cache/apk/* \  
&& find / -type f -iname \\*.apk-new -delete \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]

