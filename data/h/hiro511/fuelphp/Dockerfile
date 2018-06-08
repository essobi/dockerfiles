# Dockerfile for FuelPHP 1.8  
FROM php:7.1-apache  
MAINTAINER Hiroaki Egashira  
  
RUN apt-get update && apt-get install -y \  
git \  
zip \  
&& docker-php-ext-install \  
pdo_mysql \  
mysqli \  
mbstring \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN git clone https://github.com/fuel/fuel.git -b 1.8/master \  
&& ./fuel/composer.phar self-update \  
&& ./fuel/composer.phar --working-dir=./fuel update \  
&& php ./fuel/oil refine install  
RUN a2enmod rewrite  
RUN sed -i -e 's/\/var\/www\/html/\/var\/www\/html\/fuel\/public/'
/etc/apache2/sites-available/000-default.conf  
  
CMD ["apache2-foreground"]  

