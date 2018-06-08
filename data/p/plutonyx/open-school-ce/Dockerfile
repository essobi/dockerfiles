FROM php:7.0-apache  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
vim \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt pdo pdo_mysql mysqli
mbstring\  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN a2enmod rewrite  
COPY . /var/www/html/  
RUN chmod o+w -R /var/www/html/protected/runtime  
RUN chmod o+w -R /var/www/html/assets/

