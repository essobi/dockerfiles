FROM php:7.0-apache  
  
COPY . /var/www/html/  
WORKDIR /var/www/html  
  
RUN apt-get update \  
&& apt-get install -y git zip unzip \  
&& curl -sS https://getcomposer.org/installer | php \  
&& ./composer.phar install  
  

