FROM php:7.0-apache  
  
RUN apt update && \  
apt install -y curl libcurl3 libcurl4-gnutls-dev  
  
RUN docker-php-ext-configure curl  
RUN docker-php-ext-install curl mysqli pdo pdo_mysql  

