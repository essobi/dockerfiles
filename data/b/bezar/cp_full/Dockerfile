FROM php:7-apache  
  
COPY . /var/www/html/  
RUN apt-get update \  
&& apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev
libmcrypt-dev \  
&& docker-php-ext-install pdo_mysql mysqli mbstring gd iconv mcrypt  
RUN a2enmod rewrite  
RUN service apache2 restart  

