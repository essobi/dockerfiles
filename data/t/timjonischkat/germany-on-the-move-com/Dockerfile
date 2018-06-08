FROM php:5.6-apache  
  
RUN apt-get update && apt-get install -y git zlib1g-dev nodejs-legacy npm wget  
  
RUN docker-php-ext-install zip  
  
RUN a2enmod rewrite  
  
RUN npm install bower -g  
  
ADD . /var/www/html  
  
WORKDIR /var/www/html  
  
RUN sh install-composer.sh  
  
# TODO bower install  
RUN php composer.phar install  
  
RUN bower install --allow-root  

