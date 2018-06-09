FROM php:7.2-apache  
MAINTAINER Surasak V24 <surasakv24@gmail.com>  
RUN apt-get update \  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
git \  
zlib1g-dev \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install zip exif pdo_mysql gd  
COPY ./sites-available/laravel.conf /etc/apache2/sites-available/laravel.conf  
RUN a2dissite 000-default.conf \  
&& a2ensite laravel.conf \  
&& a2enmod rewrite  

