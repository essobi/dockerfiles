FROM php:fpm  
MAINTAINER whitecat.chayakorn@gmail.com  
ENV PHP_INI_DIR /var/www/html  
RUN mkdir -p $PHP_INI_DIR/public  
RUN apt-get update  
RUN apt-get install -y autoconf g++ make openssl libssl-dev libcurl4-openssl-
dev pkg-config libsasl2-dev libpcre3-dev  
RUN pecl install mongodb  
RUN docker-php-ext-install bcmath  
RUN echo "extension=mongodb.so" >> /usr/local/etc/php/conf.d/php.ini  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev  
  
RUN docker-php-ext-install iconv mcrypt mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  

