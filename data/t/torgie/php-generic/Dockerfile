FROM php:7-apache  
MAINTAINER "Torgie <torgie@gmail.com>"  
# Helpful for application rooted in the web directory  
ENV APPROOT /var/www  
  
# Extension/Module dependencies  
RUN apt-get update && apt-get install -y \  
git \  
libmcrypt-dev  
  
# Common extensions  
RUN docker-php-ext-install \  
bcmath \  
mcrypt \  
mysqli \  
pdo_mysql  
  
# Common modules  
RUN a2enmod rewrite  
  
WORKDIR /var/www  

