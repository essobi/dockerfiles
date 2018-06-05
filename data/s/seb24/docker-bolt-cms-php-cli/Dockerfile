FROM php:7.1-cli-alpine3.4  
  
# Upgrade the system  
RUN apk update && apk upgrade  
  
# Install curl  
RUN apk add curl-dev && docker-php-ext-install curl  
  
# Install gd  
RUN apk add libpng-dev && docker-php-ext-install gd  
  
# Install intl  
RUN apk add icu-dev && docker-php-ext-install intl  
  
# Install XML  
RUN apk add libxml2-dev && docker-php-ext-install xml  
  
# Install standalone dependencies  
RUN docker-php-ext-install \  
pdo_mysql \  
mbstring \  
opcache \  
posix \  
fileinfo \  
exif \  
zip  

