FROM php:5.6-fpm  
#  
# Mathieu GOULIN - 12/01/2016 - Version initiale  
#  
MAINTAINER Gorg Docker Maintainers "roots@asso.gadz.org"  
  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  

