# Get Base Image  
FROM php:5.6.24-apache  
  
# Install dependencies for wordpress  
RUN apt-get update && \  
apt-get install -y libpng-dev && \  
docker-php-ext-install mysql gd && \  
a2enmod rewrite  

