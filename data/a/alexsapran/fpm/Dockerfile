FROM php:5.6-fpm  
  
MAINTAINER Alexandros Sapranidis <alexsapran@gmail.com>  
  
RUN usermod -u 1000 www-data  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure mcrypt \--with-mcrypt=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysql mysqli pdo pdo_mysql \  
&& docker-php-ext-configure calendar --enable-calendar \  
&& docker-php-ext-install calendar \  
&& docker-php-ext-install mbstring  
#&& docker-php-ext-install openssl  
  
COPY php.ini /usr/local/etc/php/  
  
USER www-data  
  
CMD ["php-fpm"]  

