FROM php:5.6-apache  
  
ENV VERSION 3.8.3  
ENV PHP_TIMEZONE UTC  
  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
  
RUN docker-php-ext-install mysqli  
  
COPY php.ini /usr/local/etc/php  
  
RUN cd /tmp \  
&& curl "https://codeload.github.com/Dolibarr/dolibarr/tar.gz/${VERSION}" -o
dolibarr.tar.gz \  
&& tar -xzf dolibarr.tar.gz \  
&& cp -R dolibarr-$VERSION/htdocs/. /var/www/html \  
&& rm -R dolibarr-$VERSION  
  
RUN chown -hR www-data:www-data /var/www/html  
  
EXPOSE 80  

