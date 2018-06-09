FROM php:7.1-apache  
  
RUN apt-get update && apt-get -y install git unzip zlib1g-dev libpq-dev
libmcrypt-dev  
RUN docker-php-ext-install pdo pdo_pgsql zip mcrypt  
RUN pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug  

