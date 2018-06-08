FROM php:7.2.3-apache  
  
RUN apt-get update && apt-get install -y \  
libicu-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install zip  

