FROM php:5.6-apache  
  
RUN a2enmod rewrite  
RUN echo "ServerName www.inventid.nl" >> /etc/apache2/apache2.conf  
COPY data/php.ini /usr/local/etc/php/  
COPY site/ /var/www/html/  
  
CMD ["apache2-foreground"]  

