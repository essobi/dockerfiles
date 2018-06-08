FROM php:7.0-apache  
RUN apt-get update && apt-get install -y mysql-client libmysqlclient-dev \  
&& docker-php-ext-install mysqli  
COPY . /var/www/html/  

