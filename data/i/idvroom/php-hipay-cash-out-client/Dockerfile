FROM php:7.1-cli  
  
MAINTAINER Brice Flaceliere <contact@b-flaceliere.fr>  
  
RUN apt-get update \  
&& apt-get install -y \  
libbz2-dev \  
libssl-dev \  
ssl-cert \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libicu-dev \  
libxslt-dev \  
&& docker-php-ext-install soap xmlrpc \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug  

