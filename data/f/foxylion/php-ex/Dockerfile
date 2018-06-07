FROM php:7.1-apache  
  
RUN apt-get update && apt-get install -y unzip zip  
RUN a2enmod rewrite  
RUN docker-php-ext-install mysqli pdo pdo_mysql  
RUN sed -i '1 a \ SetEnvIfNoCase X-Forwarded-Proto https HTTPS=on'
/etc/apache2/sites-enabled/000-default.conf  

