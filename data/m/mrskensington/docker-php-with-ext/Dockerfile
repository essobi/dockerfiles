FROM php:5.6  
  
MAINTAINER docker@mikeditum.co.uk  
  
RUN apt-get update && \  
apt-get install -y libmagickwand-dev libldap2-dev && \  
apt-get clean  
  
RUN pecl install imagick && \  
docker-php-ext-enable imagick  
  
RUN docker-php-ext-install -j$(nproc) mysqli && \  
docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
docker-php-ext-configure ldap \--with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap && \  
docker-php-ext-install -j$(nproc) exif && \  
docker-php-ext-install -j$(nproc) zip && \  
docker-php-ext-install -j$(nproc) pcntl  

