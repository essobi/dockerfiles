FROM php:5.5.37-cli  
  
MAINTAINER Hayden King  
  
RUN apt-get update && apt-get install -y mysql-client libmysqlclient-dev \  
libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev libsqlite3-dev
\  
&& docker-php-ext-install iconv mcrypt pdo_mysql pdo_sqlite \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install mbstring  
  
# xdebug  
RUN pecl install xdebug-2.3.3  
COPY xdebug.ini.dist /usr/local/etc/php/conf.d/xdebug.ini  

