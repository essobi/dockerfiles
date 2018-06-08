FROM php:7-apache  
  
MAINTAINER Haijun (Navy) Su <navysu@gmail.com>  
  
RUN apt-get update && apt-get install -y ssmtp && rm -r /var/lib/apt/lists/*  
  
ADD conf/php-smtp.ini /usr/local/etc/php/conf.d/php-smtp.ini  

