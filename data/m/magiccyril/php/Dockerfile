FROM php:7-fpm  
MAINTAINER "Cyril Gravelier" <cyril@18ruedivona.eu>  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install pdo pdo_mysql  
COPY php.ini /usr/local/etc/php/  
EXPOSE 9000  
VOLUME /var/www/html  
CMD ["php-fpm"]

