FROM php:7.0.4-fpm  
  
MAINTAINER Personare <devops@personare.com.br>  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
curl \  
unzip \  
libmcrypt-dev && \  
docker-php-ext-install \  
mysqli \  
mbstring \  
pdo \  
pdo_mysql \  
mcrypt && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
WORKDIR /var/www/html  

