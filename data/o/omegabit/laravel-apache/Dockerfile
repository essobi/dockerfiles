FROM php:5.6.15-apache  
  
RUN apt-get update -qq  
RUN apt-get upgrade -qq  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev  
RUN docker-php-ext-install iconv mcrypt mbstring  
RUN a2enmod rewrite  

