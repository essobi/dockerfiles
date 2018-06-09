FROM php:7.1-apache  
  
COPY src /var/www/html  
  
ENV APACHE_DOCUMENT_ROOT /var/www/html/public  
  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
  

