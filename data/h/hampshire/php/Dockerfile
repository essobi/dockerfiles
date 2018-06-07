FROM php:7.2-fpm-stretch  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg-dev \  
libpng-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include \--with-jpeg-
dir=/usr/include \  
&& docker-php-ext-install gd mysqli pdo_mysql \  
&& rm -rf /var/lib/apt/lists/*  

