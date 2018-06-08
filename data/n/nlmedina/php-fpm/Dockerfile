FROM php:7.2-fpm  
  
MAINTAINER Nico Lance Medina <nico@nlmedina.com>  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
libcurl4-gnutls-dev \  
libicu-dev \  
libxml2-dev \  
zlib1g-dev \  
g++ \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd iconv mbstring intl curl zip xml pdo
pdo_mysql \  
&& echo "php_admin_flag[log_errors] = on" >> /usr/local/etc/php-
fpm.d/docker.conf  

