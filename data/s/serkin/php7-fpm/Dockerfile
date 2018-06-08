FROM php:fpm  
  
MAINTAINER serkin.alexander@gmail.com  
  
WORKDIR /var/www/app  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y git libssl-dev
wget nginx supervisor  
RUN docker-php-ext-install zip mbstring pdo pdo_mysql  
  
# Install Composer  
ENV COMPOSER_VERSION 1.2.0  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION}  
  
# Install Prestissimo  
RUN /usr/local/bin/composer global require hirak/prestissimo  

