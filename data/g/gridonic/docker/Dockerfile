FROM php:7.1-cli  
  
MAINTAINER Peter Siska "pesche@gridonic.ch"  
  
COPY config/99_custom.ini /usr/local/etc/php/conf.d/  
  
RUN apt-get update && apt-get install -y \  
zlib1g-dev \  
libicu-dev \  
libpq-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev && \  
  
docker-php-ext-install -j$(nproc) opcache && \  
docker-php-ext-install -j$(nproc) intl && \  
docker-php-ext-install -j$(nproc) mbstring && \  
docker-php-ext-install -j$(nproc) pdo_mysql && \  
docker-php-ext-install -j$(nproc) pdo_pgsql && \  
docker-php-ext-install -j$(nproc) zip && \  
docker-php-ext-install -j$(nproc) iconv && \  
docker-php-ext-install -j$(nproc) mcrypt && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
# Install git and curl  
apt-get install -y git curl && \  
# APCu  
pecl install apcu-5.1.8 && \  
docker-php-ext-enable apcu && \  
# Imagick  
apt-get install -y libmagickwand-dev && \  
pecl install imagick && \  
docker-php-ext-enable imagick && \  
# Clean up  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  

