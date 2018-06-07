FROM php:5.6-apache  
MAINTAINER Gaurav Malhotra <gaurav@level5websites.com>  
  
VOLUME ["/var/log/apache2"]  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install mbstring iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install bcmath gettext mysql mysqli pdo pdo_mysql  
RUN docker-php-ext-install opcache zip  
RUN apt-get install -y mysql-client  
RUN a2enmod rewrite  
  
EXPOSE 80

