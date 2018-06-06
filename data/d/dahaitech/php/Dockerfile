FROM php:5.6-fpm-alpine  
  
RUN docker-php-ext-enable opcache  
  
RUN apk add --no-cache libmcrypt-dev && docker-php-ext-install mcrypt  
  
RUN docker-php-ext-install mysql  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install pdo_mysql  
  
RUN apk add --no-cache libpng-dev libjpeg-turbo-dev freetype-dev\  
&& docker-php-ext-configure gd --with-png-dir --with-jpeg-dir --with-freetype-
dir\  
&& docker-php-ext-install gd  

