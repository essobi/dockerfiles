FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y git libmcrypt-dev mysql-client libpq-
dev iputils-ping \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install mcrypt pdo pdo_mysql pdo_pgsql pgsql pcntl  
  
WORKDIR /var/www  

