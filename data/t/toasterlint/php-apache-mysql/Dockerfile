FROM php:7.2-apache  
MAINTAINER Henry Mohn <henry@toasterlint.com>  
  
# Enable Apache Rewrite Module  
RUN a2enmod rewrite  
  
# Install PHP extensions  
RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev zip unzip &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
  
RUN echo "error_reporting = E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED &
~E_WARNING" > /usr/local/etc/php/php.ini  
  
VOLUME /var/www/html  
  
CMD ["apache2-foreground"]  

