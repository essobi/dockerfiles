FROM php:7.1-fpm-alpine  
  
RUN apk update && apk add \  
libmcrypt-dev \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
autoconf \  
&& rm /var/cache/apk/*  
  
RUN docker-php-ext-install iconv  
RUN docker-php-ext-install mcrypt  
  
RUN docker-php-ext-install gd  
  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer \  
&& chmod +x /usr/bin/composer  
  
RUN composer global require hirak/prestissimo  
  
WORKDIR /var/www  
  

