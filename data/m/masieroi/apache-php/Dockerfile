# Version 0.0.1  
FROM php:5.6.30-apache  
  
MAINTAINER Ivano Masiero <info@ivanomasiero.com>  
  
ENV TERM=xterm  
  
RUN apt-get update && apt-get install -y \  
nano \  
git \  
zip \  
locate  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN updatedb  
  
RUN a2enmod rewrite  
  
RUN docker-php-ext-install pdo pdo_mysql mysqli  

