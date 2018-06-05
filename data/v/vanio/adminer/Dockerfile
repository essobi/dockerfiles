FROM php:5-apache  
  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
wget && \  
docker-php-ext-install pgsql && \  
docker-php-ext-install pdo_pgsql && \  
docker-php-ext-install mysql && \  
docker-php-ext-install pdo_mysql  
  
RUN wget https://www.adminer.org/latest.php -O index.php  
  
COPY php.ini /usr/local/etc/php/  

