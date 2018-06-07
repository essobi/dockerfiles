FROM php:7.2-zts-alpine  
  
# add source  
ADD index.php /var/www/html/index.php  
  
# add user apache  
RUN chown www-data:www-data /var/www/html -R  
  
# change user container  
USER www-data  
  
EXPOSE 8000  
  
CMD php -S 0.0.0.0:8000 -t /var/www/html

