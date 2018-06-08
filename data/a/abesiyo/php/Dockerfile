FROM php:5.6-apache  
  
MAINTAINER Alberto Contreras <abecontreras@me.com>  
  
RUN a2enmod rewrite  
  
# Install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev
libmcrypt-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip json mcrypt  
  
COPY bashrc /root/.bashrc  
  
WORKDIR /var/www/html  
  
RUN chown -R www-data:www-data /var/www  
  
VOLUME ["/var/log/apache2"]  

