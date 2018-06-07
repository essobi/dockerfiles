FROM php:7.1.11-apache-jessie  
  
# Install system dependencies  
RUN apt-get update  
RUN apt-get -qq install libpng-dev libfreetype6-dev libjpeg-dev git  
  
# Install mysqli extension for PHP  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install mysqli gd zip  
  
# Install xdebug  
RUN pecl install xdebug-2.6.0 && docker-php-ext-enable xdebug  
  
# Enable mod rewrite  
RUN a2enmod rewrite  
  
# Create self signed certificate  
RUN openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout
/etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-
selfsigned.crt -subj "/C=DE/ST=Denial/L=Springfield/O=Dis/CN=www.example.com"  
  
# Enable ssl  
RUN sed -i 's/ssl-cert-snakeoil.pem/apache-selfsigned.crt/g'
/etc/apache2/sites-available/*.conf  
RUN sed -i 's/ssl-cert-snakeoil.key/apache-selfsigned.key/g'
/etc/apache2/sites-available/*.conf  
RUN a2enmod ssl && a2enmod headers && a2ensite default-ssl  
  
# Set apache document root  
ENV APACHE_DOCUMENT_ROOT /var/www/web  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
  
# Copy config file  
COPY php.ini /usr/local/etc/php  
  
# Set workdir  
WORKDIR ${APACHE_DOCUMENT_ROOT}  
  

