FROM php:7.2-apache  
COPY src/ /var/www/html  
COPY build.php /var/www/html/build.php  
RUN docker-php-ext-install mysqli  
RUN php /var/www/html/build.php  
RUN a2enmod rewrite  
RUN a2enmod headers  
RUN service apache2 restart  
EXPOSE 80

