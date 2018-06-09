FROM php:5.4-apache  
# Install modules  
RUN apt-get update && apt-get install -y zlib1g-dev  
RUN docker-php-ext-install mysql mysqli pdo pdo_mysql mbstring zip  
# && docker-php-ext-configure zip \--with-zlib-dir=/usr/src/php/ext/zlib/ \  
# && docker-php-ext-install zip  
#CMD ["apache2-foreground"]  

