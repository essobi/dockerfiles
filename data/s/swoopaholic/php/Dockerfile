FROM php:5-fpm  
MAINTAINER Danny Dörfel <danny.dorfel@gmail.com>  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install opcache  
  
RUN apt-get install -y \  
libssl-dev \  
&& cd /usr/src/php \  
&& pecl install mongo \  
&& make clean  
  
RUN echo "extension=mongo.so" > /usr/local/etc/php/conf.d/docker-php-ext-
mongo.ini  
RUN echo "date.timezone=Europe/Amsterdam" > /usr/local/etc/php/php.ini  
  
RUN usermod -u 501 www-data  
  
RUN mkdir -p /var/www  
  
CMD ["php-fpm"]  

