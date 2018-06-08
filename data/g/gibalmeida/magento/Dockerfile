FROM php:5.6-apache  
MAINTAINER Gilberto Cezar de Almeida <gibalmeida@gmail.com>  
COPY config/php.ini /usr/local/etc/php/  
RUN apt-get update && apt-get install -y \  
libcurl3-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include --with-jpeg-
dir=/usr/include \  
&& docker-php-ext-install -j$(nproc) \  
curl \  
gd \  
mcrypt \  
pdo_mysql \  
soap \  
xml \  
xsl \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& a2enmod rewrite  
  
  

