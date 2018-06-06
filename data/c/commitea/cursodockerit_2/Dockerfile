#Dockerfile para instalar apache y php en version 7  
#comentario 5  
FROM php:7-apache  
MAINTAINER commitea <armolinamilla@gmail.com>  
  
COPY php.ini /usr/local/etc/php/  
COPY index.php /var/www/html  
  
#ejecuto la instalación de librerias nuevas  
RUN apt-get update \  
&& apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev
libmcrypt-dev \  
&& docker-php-ext-install pdo_mysql mysqli mbstring gd iconv mcrypt  
  
RUN apt-get install -y vim \  
&& apt-get install -y nano  
  
EXPOSE 80  
WORKDIR /var/www/html  
  
#fin del Dockerfile  

