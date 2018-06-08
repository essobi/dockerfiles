FROM php:7.0.2-fpm  
  
RUN apt-get update  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
git \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd pdo pdo_mysql mbstring zip mysqli  
  
RUN mkdir /var/log/php-fpm  
RUN touch /var/log/php-fpm/error.log /var/log/php-fpm/access.log  
RUN chown www-data:www-data /var/log/php-fpm -R  
RUN chmod 664 /var/log/php-fpm -R  

