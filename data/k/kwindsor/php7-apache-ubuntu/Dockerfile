FROM php:7.1-apache  
  
RUN apt-get update && apt-get install -y  
  
# MySQL  
RUN apt-get install -y mysql-client libmysqlclient-dev && docker-php-ext-
install mysqli  
  
# PDO  
RUN docker-php-ext-install pdo pdo_mysql  
  
# GD for image processing  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
# Mail  
RUN apt-get update && apt-get install -y sendmail  
  
# Enable rewrite rules (ie. to route all requests to index.php)  
RUN a2enmod rewrite  

