FROM php:7.0-apache  
RUN apt-get update && apt-get install -y libmagickwand-dev --no-install-
recommends && rm -rf /var/lib/apt/lists/*  
RUN apt-get install curl  
RUN pecl install imagick-beta  
RUN docker-php-ext-install pdo pdo_mysql  
RUN a2enmod rewrite  
  
#RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
ENV APACHE_DOCUMENT_ROOT /public  
  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
  
COPY src/ /var/www/html/  
# WORKDIR /var/www/html/  
# RUN composer install --no-interaction

