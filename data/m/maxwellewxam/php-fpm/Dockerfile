FROM php:fpm  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y \  
git \  
libicu-dev \  
libmcrypt-dev \  
libssl-dev \  
libxml2-dev \  
libzip-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev  
  
RUN docker-php-ext-install intl mbstring mysqli pdo_mysql ftp sockets xmlrpc
zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
RUN curl http://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
  
RUN usermod -u 1000 www-data  

