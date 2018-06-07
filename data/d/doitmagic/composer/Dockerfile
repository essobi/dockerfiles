FROM phusion/baseimage:0.9.17  
MAINTAINER Doitmagic <razvan@doitmagic.com>  
  
ENV COMPOSER_VERSION=1.1.2  
RUN mkdir -p /var/www  
  
RUN apt-get update && apt-get install -y --force-yes php5 php5-fpm php5-cli
php5-mysql php5-mcrypt php5-gd php5-curl php5-intl  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
VOLUME [/var/www]  
  
WORKDIR /var/www  

