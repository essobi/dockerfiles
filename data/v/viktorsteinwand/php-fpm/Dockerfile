FROM php:7.0-fpm  
  
# Install tools required to enable installing extensions  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev libicu-dev g++ wget \  
&& apt-get purge -y --auto-remove  
  
# Install extensions required by Symfony  
RUN /usr/local/bin/docker-php-ext-install \  
intl \  
opcache \  
pdo_mysql \  
mysqli \  
mbstring \  
hash \  
bcmath \  
json \  
zip  
  
COPY php.ini /usr/local/etc/php/php.ini  

