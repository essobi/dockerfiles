FROM php:7.1-apache  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get install -y wget unzip  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer  
  
# Install project dependencies  
WORKDIR /var/www  
COPY composer.json .  
# COPY composer.lock .  
RUN composer install --no-scripts --no-autoloader --no-dev  
  
# Install project src  
COPY ./ /var/www/  
  
# Execute post-install steps  
RUN composer dump-autoload --optimize  

