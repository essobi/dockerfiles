FROM php:5.6-apache  
  
RUN apt-get update -y && apt-get install -y sendmail libpng-dev libtidy-dev
libfreetype6-dev libjpeg62-turbo-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd mysql mysqli tidy  
RUN a2enmod rewrite  
RUN a2enmod headers  
  
COPY php.ini /usr/local/etc/php/  

