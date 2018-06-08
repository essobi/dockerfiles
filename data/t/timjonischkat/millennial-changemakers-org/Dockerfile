FROM php:5.6-apache  
  
RUN apt-get update  
  
RUN apt-get install -y git zlib1g-dev  
  
RUN docker-php-ext-install zip  
  
RUN a2enmod rewrite  
  
#ADD ./docker/apache2.conf /etc/apache2/apache2.conf  
ADD . /var/www/html  
  
WORKDIR /var/www/html

