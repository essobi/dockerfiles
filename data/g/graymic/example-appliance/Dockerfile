FROM composer:latest  
  
COPY blog /app  
  
RUN composer install  
  
FROM php:7.0-apache  
  
ENV APACHE_DOCUMENT_ROOT /var/www/html/public  
  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
  
COPY \--from=0 /app .  
  
RUN usermod -u 1000 www-data  
RUN chown -R www-data:www-data /var/www/html  

