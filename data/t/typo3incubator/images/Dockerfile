FROM php:5.6-fpm  
  
MAINTAINER Frank Nägler <frank.naegler@typo3.com>  
MAINTAINER Oliver Hader <oliver.hader@typo3.org>  
  
# Fix docker-php-ext-install script error  
RUN sed -i 's/docker-php-\\(ext-$ext.ini\\)/\1/' /usr/local/bin/docker-php-
ext-install  
  
# Install other needed extensions  
RUN apt-key update && \  
apt-get clean && \  
apt-get purge && \  
apt-get update && \  
apt-get install -y graphicsmagick &&\  
apt-get install -y mysql-client && \  
apt-get install -y ssh git && \  
apt-get install -y rsync && \  
apt-get install -y ssmtp && \  
apt-get install -y libfreetype6-dev libjpeg62-turbo-dev && \  
apt-get install -y libldap2-dev && \  
apt-get install -y libxml2-dev && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap && \  
docker-php-ext-install soap && \  
docker-php-ext-install zip && \  
docker-php-ext-install mysqli && \  
docker-php-ext-install pdo pdo_mysql && \  
docker-php-ext-install mbstring && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd  

