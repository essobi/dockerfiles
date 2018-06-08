FROM php:5.6-fpm  
RUN apt-get update && apt-get install -y libpq-dev postgresql php5-pgsql  
RUN docker-php-ext-install mbstring pdo_mysql pdo_pgsql  

