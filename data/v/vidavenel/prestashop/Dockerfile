FROM php:5.5-apache  
MAINTAINER Vincent DAVENEL <vincent@aiglecom.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y libmcrypt-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libfreetype6-dev \  
libxml2-dev \  
wget \  
unzip \  
libmemcached-dev \  
curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install iconv mcrypt pdo pdo_mysql mbstring soap gd  
  
VOLUME /var/www/html  
  
# Apache configuration  
RUN a2enmod rewrite  
RUN chown www-data:www-data -R /var/www/html/  
  
# PHP configuration  
COPY php.ini /usr/local/etc/php/  
  
RUN usermod -u 1000 www-data  

