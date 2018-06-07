FROM whitehart/nginx-php-7  
WORKDIR /var/www/html/  
  
COPY composer.json ./  
COPY composer.lock ./  
RUN composer install --no-scripts --no-autoloader --no-interaction  
  
COPY . ./  
RUN composer dump-autoload --optimize

