FROM php:7.2-fpm  
WORKDIR /app  
RUN apt-get -yqq update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
apt-utils \  
libzip-dev \  
libpng-dev \  
libfreetype6-dev \  
libjpeg-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
autoconf \  
g++ \  
make \  
openssl \  
libssl-dev \  
libcurl4-openssl-dev \  
pkg-config \  
libsasl2-dev \  
libpcre3-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
;  
  
# Install some php extensions.  
RUN pecl install mcrypt-1.0.1 \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install \  
mysqli \  
pdo_mysql \  
gd \  
&& docker-php-ext-enable mcrypt \  
;  

