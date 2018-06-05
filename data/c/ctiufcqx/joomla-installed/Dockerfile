FROM php:5.6-apache  
MAINTAINER Coordenadoria de Tecnologia da Informação <ccti@quixada.ufc.br>  
  
# Enable Apache Rewrite Module  
RUN a2enmod rewrite  
  
# Install PHP extensions  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev zip unzip &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
  
VOLUME /var/www/html  
  
CMD ["apache2-foreground"]  

