FROM php:7.1-cli  
  
MAINTAINER Branko Ajzele <branko@foggyline.net>  
  
RUN apt-get update && apt-get install -y \  
cron \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
mysql-client \  
zip  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ \--with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install \  
bcmath \  
gd \  
intl \  
mbstring \  
mcrypt \  
opcache \  
pdo_mysql \  
soap \  
xsl \  
zip  
  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer  

