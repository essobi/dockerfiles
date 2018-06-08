# docker build -t snowsprout/php7.1-fpm .  
FROM php:7.1-fpm  
  
MAINTAINER "SnowSprout" <me@snowsprout.net>  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
libxml2-dev \  
libssl-dev  
  
# Install Exts  
RUN docker-php-ext-install dom  
  
RUN docker-php-ext-install mbstring  
  
RUN docker-php-ext-install mcrypt  
  
RUN docker-php-ext-install mysqli  
  
RUN docker-php-ext-install pdo_mysql  
  
RUN pecl install mongodb \  
&& docker-php-ext-enable mongodb

