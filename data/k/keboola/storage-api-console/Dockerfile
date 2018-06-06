FROM php:7.0.2-apache  
  
ARG KEBOOLA_SAPI_CONSOLE_VERION  
ENV KEBOOLA_SAPI_CONSOLE_VERION=$KEBOOLA_SAPI_CONSOLE_VERION  
  
RUN a2enmod rewrite  
RUN a2enmod headers  
  
COPY ./php-apache/storage-api-console.conf /etc/apache2/sites-enabled/storage-
api-console.conf  
COPY ./php-apache/security.conf /etc/apache2/conf-enabled/security.conf  
COPY index.php /var/www/html/index.php  

