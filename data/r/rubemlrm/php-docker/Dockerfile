FROM php:7.1-fpm  
MAINTAINER Rubem Mota <rubemmota89@gmail.com>  
  
#enable mcrypt iconv and gd extensions  
RUN apt-get update && apt-get install -y \  
git \  
libaspell-dev \  
libbz2-dev \  
libcurl4-gnutls-dev \  
libexpat1-dev \  
libfreetype6-dev \  
libgmp3-dev \  
libicu-dev \  
libjpeg-dev \  
libjpeg62-turbo-dev \  
libldap2-dev \  
libmcrypt-dev \  
libpcre3-dev \  
libpng-dev \  
libpng12-dev \  
libpq-dev \  
libsnmp-dev \  
libsqlite3-dev \  
libvpx-dev \  
libxml2-dev \  
libxpm-dev \  
unixodbc-dev \  
zlib1g-dev \  
libtidy-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install curl \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install xml \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install bz2 \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install json  
  
RUN pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug  
  
# Enable some pdo mysql extensions  
RUN docker-php-ext-install pdo pdo_mysql

