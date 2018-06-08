FROM mileschou/phalcon:7.0-apache  
  
RUN apt-get update  
  
COPY etc/apache2/apache2.conf /etc/apache2/apache2.conf  
RUN a2enmod rewrite  
  
RUN docker-php-ext-install pdo_mysql  
  
RUN apt-get install libpng12-dev -y  
RUN docker-php-ext-install gd

