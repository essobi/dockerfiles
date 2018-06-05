FROM php:7.0-apache  
  
RUN apt-get -y update && apt-get install -y \  
wget \  
git \  
zlib1g-dev  
RUN docker-php-ext-install zip  
  
RUN sed -i 's/DocumentRoot .*$/DocumentRoot \/var\/www\/html\/web/'
/etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
RUN mkdir /var/www/.composer && chown www-data:www-data /var/www/.composer  
  
COPY . /var/www/html/  
  
RUN chown -R www-data:www-data /var/www/html  
  
RUN cd /var/www/html \  
&& bash scripts/install-composer.sh \  
&& php composer.phar install  

