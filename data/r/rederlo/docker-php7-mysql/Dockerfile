FROM php:7.0-apache  
MAINTAINER ederlo.contato@gmail.com  
  
RUN apt-get update && apt-get install -y vim  
  
#install pdo  
RUN docker-php-ext-install pdo pdo_mysql  
  
# Install intl  
RUN apt-get install -y libicu-dev  
RUN pecl install intl  
RUN docker-php-ext-install intl  
  
#install mbstring  
RUN docker-php-ext-install mbstring  
  
# Install GD  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  
RUN docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/  
RUN docker-php-ext-install gd  
  
# Install mcrypt  
RUN apt-get install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  

