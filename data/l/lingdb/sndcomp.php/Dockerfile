FROM php:7-apache  
  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="sndcomp.php" \  
version="1.1.1" \  
documentation="https://github.com/lingdb/container/wiki/sndcomp.php"  
  
RUN docker-php-ext-install mysqli \  
&& a2enmod rewrite \  
&& apt-get update \  
&& apt-get install -y git \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY php.ini /usr/local/etc/php/  
  
COPY src/ /var/www/html  
  
RUN chmod -R 777 /var/www/html/export/download  

