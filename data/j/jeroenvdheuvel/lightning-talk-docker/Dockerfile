FROM php:5.6-apache  
  
MAINTAINER Jeroen van den Heuvel  
  
RUN apt-get update && \  
apt-get install -y zlib1g-dev git && \  
docker-php-ext-install zip && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www/html  
  
COPY ./composer.* ./  
  
RUN curl -sS https://getcomposer.org/installer | php && \  
php composer.phar install --prefer-dist --no-scripts && \  
rm composer.phar  
  
COPY ./ ./  
  
RUN ./vendor/bin/phpunit  
  
EXPOSE 80  

