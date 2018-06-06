FROM php:7.0-apache  
RUN docker-php-ext-install pdo pdo_mysql  
COPY ./src /var/www/html/  
RUN chown -R www-data:www-data /var/www/html/  

