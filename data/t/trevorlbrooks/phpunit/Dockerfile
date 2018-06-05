FROM php:5-jessie  
  
MAINTAINER Trevor Brooks <tbrooks@mtech.edu>  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
RUN apt-get update -yqq  
RUN apt-get install -yqq git \  
libmcrypt-dev libpq-dev libcurl4-gnutls-dev \  
libicu-dev libvpx-dev libjpeg-dev \  
libpng-dev libxpm-dev zlib1g-dev \  
libfreetype6-dev libxml2-dev libexpat1-dev \  
libbz2-dev libgmp3-dev libldap2-dev \  
unixodbc-dev libsqlite3-dev libaspell-dev \  
libsnmp-dev libpcre3-dev libtidy-dev mysql-client  
RUN docker-php-ext-install mbstring mcrypt \  
curl json gd xml zip \  
bz2 opcache pdo_mysql  
#RUN curl -sS https://getcomposer.org/installer | php && php composer.phar
install  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
  
EXPOSE 80 443  

