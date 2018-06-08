FROM php:apache  
MAINTAINER Seti <seti@setadesign.net>  
  
RUN a2enmod rewrite  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
&& docker-php-ext-install -j$(nproc) mysqli bcmath session \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd

