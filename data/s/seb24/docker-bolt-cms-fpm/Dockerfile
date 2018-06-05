FROM php:7.1-fpm-alpine3.4  
  
# Custom www.conf to activate environment variables  
COPY config/www.conf /usr/local/etc/php-fpm.d/www.conf  
  
# Upgrade the system  
RUN apk update && apk upgrade  
  
# Install curl  
RUN apk add curl-dev && docker-php-ext-install curl  
  
# Install gd  
RUN apk add libpng-dev libjpeg-turbo-dev freetype-dev \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# Install intl  
RUN apk add icu-dev && docker-php-ext-install intl  
  
# Install XML  
RUN apk add libxml2-dev && docker-php-ext-install xml  
  
# Install standalone dependencies  
RUN docker-php-ext-install \  
mysqli \  
pdo \  
pdo_mysql \  
mbstring \  
opcache \  
posix \  
fileinfo \  
exif \  
zip  

