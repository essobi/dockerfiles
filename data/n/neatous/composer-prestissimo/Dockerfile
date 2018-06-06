FROM php:7.2-alpine  
MAINTAINER Martin Venuš <martin.venus@gmail.com>  
  
RUN apk --update add git tar zip zlib-dev && \  
docker-php-ext-install zip && \  
php -r "readfile('https://getcomposer.org/installer');" | php -- --install-
dir=bin --filename=composer && \  
composer global require hirak/prestissimo  
  
WORKDIR /app  
  
ENTRYPOINT ["composer"]  

