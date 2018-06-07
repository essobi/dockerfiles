FROM php:7.1-cli  
  
MAINTAINER Uwe Kleinmann <u.kleinmann@kellerkinder.de>  
  
RUN apt-get update -yqq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ant \  
build-essential \  
git \  
wget \  
zip \  
unzip \  
mysql-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmagickwand-6.q16-dev \  
imagemagick-6.q16 \  
ghostscript \  
libmcrypt-dev \  
libpng12-dev \  
libssl-dev \  
libxml2-dev \  
libicu-dev \  
libcurl4-openssl-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& docker-php-source extract \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install -j$(nproc) intl \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& docker-php-ext-install -j$(nproc) pdo \  
&& docker-php-ext-install -j$(nproc) pdo_mysql \  
&& docker-php-ext-install -j$(nproc) xml \  
&& docker-php-ext-install -j$(nproc) zip \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& docker-php-source delete  
  
COPY clone-shopware /usr/local/bin/  

