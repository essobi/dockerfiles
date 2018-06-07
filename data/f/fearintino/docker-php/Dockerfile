FROM php:7.1-fpm-alpine  
  
MAINTAINER Timur Mukhtarov  
  
ADD php.ini /usr/local/etc/php/  
  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
icu-dev \  
zlib-dev  
  
RUN apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev
libjpeg-turbo-dev postgresql-dev && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
docker-php-ext-install -j${NPROC} gd pdo pdo_pgsql pgsql exif zip bcmath intl
mysqli pdo_mysql && \  
pecl install xdebug && \  
docker-php-ext-enable pdo pdo_pgsql pgsql exif zip xdebug bcmath intl mysqli
pdo_mysql && \  
apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev  
  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/bin/composer  
RUN composer global require "hirak/prestissimo:^0.3"  

