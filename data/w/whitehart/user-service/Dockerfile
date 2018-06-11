FROM whitehart/nginx-php-7  
WORKDIR /var/www/html/  
  
COPY composer.json ./  
COPY composer.lock ./  
RUN composer install --no-scripts --no-autoloader  
  
COPY . ./  
RUN composer dump-autoload --optimize

