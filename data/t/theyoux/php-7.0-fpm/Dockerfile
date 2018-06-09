FROM php:7.0-fpm  
MAINTAINER Loïc Caillieux <loic@emagma.fr>  
  
RUN \  
apt-get update \  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libxslt1-dev \  
libpq-dev \  
&& docker-php-ext-install iconv \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install pdo \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install xsl \  
&& docker-php-ext-install pgsql \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  

