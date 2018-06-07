FROM php:7.0-fpm  
MAINTAINER apps@desmart.com  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
libbz2-dev \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libzip-dev \  
libpq-dev \  
openssl \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install bz2 curl exif iconv mbstring mcrypt mysqli pdo
pdo_mysql pdo_pgsql zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY php.ini /usr/local/etc/php/conf.d/desmart-php.ini  
  
# COPY docker-entrypoint.sh /entrypoint.sh  
# RUN chmod +x /entrypoint.sh  
# ENTRYPOINT ["/entrypoint.sh"]

