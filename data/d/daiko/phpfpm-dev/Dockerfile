FROM php:7.1-fpm  
  
  
RUN apt-get update && apt-get install -y \  
ssmtp \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
mariadb-client \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) iconv gd zip sockets mysqli pdo pdo_mysql
mbstring \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pecl install xdebug-2.5.5 \  
&& docker-php-ext-enable xdebug  
  
RUN setcap cap_net_raw=eip /usr/local/bin/php  

