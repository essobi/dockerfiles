FROM php:5.6-apache  
  
RUN apt-get update && apt-get install -y && apt-get install -y mysql-client
libmysqlclient-dev && docker-php-ext-install mysql  
  
COPY ./src /var/www/html/  
RUN mkdir /var/www/html/cache  
RUN chown -R www-data:www-data /var/www/html/  

