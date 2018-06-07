FROM php:7.1-fpm  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
wget \  
libldap2-dev \  
libxml2-dev \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev && \  
docker-php-ext-configure ldap \--with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install ldap xml mbstring curl gd && \  
apt-get clean autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}

