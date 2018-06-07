FROM php:7-fpm  
  
RUN apt-get update && \  
apt-get install -y \  
zlib1g-dev  
  
RUN docker-php-ext-install pdo pdo_mysql zip  
  
RUN apt-get install -y unzip git  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
WORKDIR /var/www  

