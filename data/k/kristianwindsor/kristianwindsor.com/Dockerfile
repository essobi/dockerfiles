FROM php:7.0-apache  
  
RUN apt-get update && apt-get install -y  
RUN a2enmod headers  
  
COPY ./src /var/www/html/  
RUN chown -R www-data:www-data /var/www/html/  

