FROM php:7.1.9-apache  
  
COPY apache-conf/apache2.conf /etc/apache2/apache2.conf  
COPY apache-conf/000-default.conf /etc/apache2/sites-
available/000-default.conf  
  
ONBUILD RUN a2enmod headers  
  

