FROM php:7.0-apache  
  
# Install modules  
RUN apt-get update && \  
apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt pdo_mysql mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN a2enmod rewrite  
  
WORKDIR /var/www/html  

