FROM php:5.6-apache  
MAINTAINER Ian Blenke <ian@blenke.com>  
  
env VERSION 1.15.4  
WORKDIR /var/www/html  
  
RUN apt-get update -y && \  
apt-get install -y wget && \  
wget
https://github.com/simplesamlphp/simplesamlphp/releases/download/v$VERSION/simplesamlphp-$VERSION.tar.gz
&& \  
tar xvzf simplesamlphp-$VERSION.tar.gz --strip-components 1 -C /var/www/html  
  
RUN cp -r config-templates/* config/ && cp -r metadata-templates/* metadata/  
  
VOLUME /var/www/html/config  
VOLUME /var/www/html/metadata  
  
# Install the gmp and mcrypt extensions  
RUN apt-get update -y && \  
apt-get install -y git re2c libmhash-dev file  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN php composer.phar install  

