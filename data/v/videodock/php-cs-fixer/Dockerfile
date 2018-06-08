FROM php:7.1.1-alpine  
  
RUN apk update && apk upgrade  
  
#Install Git, curl (for composer installation), zip/unzip which composer uses
when installing vendors  
RUN apk --update add curl git unzip && rm /var/cache/apk/*  
  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer global require friendsofphp/php-cs-fixer

