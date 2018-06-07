FROM php:7.1-fpm  
MAINTAINER Droptica <info@droptica.com>  
  
# Packages  
RUN apt-get update && apt-get install --no-install-recommends -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
mcrypt \  
libmcrypt-dev \  
libjpeg-dev \  
pkg-config libmagickwand-dev imagemagick \  
libmemcached-dev \  
zlib1g-dev libicu-dev  
  
  
RUN printf "\n" | pecl install imagick && docker-php-ext-enable imagick \  
&& echo "no" | pecl install memcached && docker-php-ext-enable memcached \  
&& pecl install redis && docker-php-ext-enable redis \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd pdo pdo_mysql mbstring zip bcmath intl
exif fileinfo \  
&& docker-php-ext-enable opcache  
  
# Time Zone  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

