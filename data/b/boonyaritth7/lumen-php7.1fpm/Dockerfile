FROM php:7.1-fpm  
  
MAINTAINER Maintaner BoonyaritTH7  
  
RUN apt-get update && apt-get upgrade -y \  
wget \  
git \  
re2c \  
apt-utils \  
apt-transport-https \  
vim \  
zip \  
lsb-release \  
build-essential \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpq-dev \  
libmagickwand-dev \  
libmcrypt-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmemcached-dev \  
libssl-dev \  
libssl-doc \  
libsasl2-dev \  
zlib1g-dev \  
&& docker-php-ext-install \  
bz2 \  
iconv \  
mbstring \  
mcrypt \  
mysqli \  
pgsql \  
pdo_mysql \  
pdo_pgsql \  
soap \  
zip \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& pecl install xdebug && docker-php-ext-enable xdebug \  
&& pecl install mongodb && docker-php-ext-enable mongodb \  
&& pecl install redis && docker-php-ext-enable redis \  
&& yes '' | pecl install imagick && docker-php-ext-enable imagick  
  
# Install composer  
RUN curl -sS --insecure https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Lumen  
RUN composer global require "laravel/lumen-installer"

