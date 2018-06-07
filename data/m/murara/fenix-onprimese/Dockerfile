FROM php:5.5.31-apache  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install soap \  
&& a2enmod rewrite \  
&& a2enmod cache \  
&& a2enmod cache_disk \  
&& a2enmod expires \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY config/php.ini /usr/local/etc/php/  

