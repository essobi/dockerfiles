FROM php:5-fpm  
MAINTAINER Diego Gullo <diegogullo@gmail.com>  
#apt-get install php5-gd php5-mcrypt php-calendar php-gettext php5-intl
php5-xdebug  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev\  
libicu-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt gettext intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& chown -R www-data:www-data /var/www \  
&& mkdir -p /var/www/portal-cache \  
&& chmod 777 /var/www/portal-cache  

