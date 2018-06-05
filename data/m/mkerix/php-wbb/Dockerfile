FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y mysql-client && rm -rf
/var/lib/apt/lists/*  
RUN docker-php-ext-install pdo_mysql  

