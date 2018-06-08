FROM php:5.6-fpm  
MAINTAINER Rhyuko <rvolhuer@gmail.com>  
  
RUN usermod -u 1000 www-data  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y curl ssmtp g++ libxml2-dev libfreetype6-dev
libjpeg62-turbo-dev libpng12-dev libgd-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd exif  
  
RUN apt-get install -y php5-mysql  
RUN docker-php-ext-install mysqli pdo pdo_mysql  
  
RUN apt-get install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
  
RUN docker-php-ext-configure opcache --enable-opcache  
RUN docker-php-ext-install opcache  
  
RUN docker-php-ext-install zip soap  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=1.2.0  
  
RUN ls -la /usr/sbin/sendmail  

