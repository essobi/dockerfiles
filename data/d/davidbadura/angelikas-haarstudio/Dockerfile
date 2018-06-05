FROM php:7-apache  
RUN apt-get update && apt-get install -y git unzip  
COPY ./ /var/www/  
RUN rm -rf /var/www/html && ln -s /var/www/web /var/www/html  
RUN cd /var/www && curl -O https://getcomposer.org/composer.phar && php
./composer.phar install  
RUN a2enmod rewrite && service apache2 restart  

