FROM php:5.6-apache  
MAINTAINER Robert Jacob <xperimental@solidproject.de>  
  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev libpng12-dev unzip  
  
RUN docker-php-ext-install gd pdo pdo_mysql zip  
  
ADD php.ini /usr/local/etc/php/php.ini  
RUN mkdir -p /var/lib/php5/sessions \  
&& chown -R www-data:www-data /var/lib/php5/sessions  
  
ADD http://thinkup.com/download/ /tmp/thinkup.zip  
RUN unzip /tmp/thinkup.zip -d /tmp/ \  
&& mv /tmp/thinkup/* /var/www/html \  
&& chown -R www-data:www-data /var/www/html  

