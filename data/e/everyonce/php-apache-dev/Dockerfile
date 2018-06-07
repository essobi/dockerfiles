FROM php:5.5-apache  
RUN a2enmod rewrite  
RUN docker-php-ext-install mysqli  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  

