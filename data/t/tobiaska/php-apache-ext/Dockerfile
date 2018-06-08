FROM php:apache  
  
RUN a2enmod rewrite  
  
RUN apt-get update -y && \  
apt-get install -y \  
libfreetype6-dev \  
libpng-dev \  
libjpeg62-turbo-dev  
  
RUN docker-php-ext-configure gd --with-jpeg-dir=/usr/include/  
RUN docker-php-ext-install gd exif  
  
RUN docker-php-ext-install mysqli  
  
RUN docker-php-ext-install bcmath  

