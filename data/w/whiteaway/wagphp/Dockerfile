FROM php:7.2-apache  
  
MAINTAINER Whiteaway Dev <dev@whiteaway.com>  
  
# Install needed system stuff  
RUN apt-get -y update \  
&& apt-get -y install --no-install-recommends unzip  
  
# Install needed php stuff  
RUN docker-php-ext-install pdo_mysql bcmath pcntl sockets \  
&& a2enmod rewrite  
  
RUN curl -sS https://getcomposer.org/installer \  
| php -- --install-dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/composer  

