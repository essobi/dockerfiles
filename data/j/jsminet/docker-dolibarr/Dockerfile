FROM php:5.6.32-apache  
MAINTAINER JS Minet  
  
ENV VERSION 6.0.4  
  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libldap2-dev
\  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap \  
&& docker-php-ext-install mysqli \  
&& apt-get purge -y libpng12-dev libjpeg-dev libldap2-dev \  
&& cd /tmp \  
&& curl "https://codeload.github.com/Dolibarr/dolibarr/tar.gz/${VERSION}" -o
dolibarr.tar.gz \  
&& tar -xzf dolibarr.tar.gz \  
&& cp -R dolibarr-$VERSION/htdocs/. /var/www/html \  
&& rm -R dolibarr-$VERSION \  
&& rm dolibarr.tar.gz \  
&& mkdir /var/www/html/documents \  
&& chown -hR www-data:www-data /var/www/html  
  
COPY php.ini /usr/local/etc/php  
  
VOLUME ["/var/www/html/conf", "/var/www/html/documents"]  
  
EXPOSE 80  

