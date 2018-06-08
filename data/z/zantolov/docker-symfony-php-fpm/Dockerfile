FROM php:7.2-fpm  
  
RUN apt-get update && apt-get install -y \  
git \  
unzip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install opcache  
  
RUN apt-get install -y libpq-dev  
RUN docker-php-ext-install pdo_pgsql  
  
ADD custom.ini /usr/local/etc/php/conf.d/custom.ini  
  
RUN useradd -m symfony  
USER symfony  
  
WORKDIR /var/www/symfony  

