FROM php:7-apache  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
libicu-dev \  
libpq-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt soap intl mysqli pdo_mysql
gettext pgsql pdo_pgsql calendar \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& rm -rf /var/lib/apt/lists/* \  
&& a2enmod rewrite \  
&& a2enmod headers  

