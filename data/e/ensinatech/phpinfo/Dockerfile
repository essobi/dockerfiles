FROM php:7-apache  
MAINTAINER thiago  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN docker-php-ext-install mysqli  
  
COPY index.php /var/www/html/  
# COPY config/php.ini /usr/local/etc/php/  

