FROM wordpress:latest  
  
RUN a2enmod ext_filter  
RUN a2enmod headers  
  
RUN pecl install redis  
RUN docker-php-ext-enable redis  

