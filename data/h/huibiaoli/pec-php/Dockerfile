FROM php:5.6-fpm  
  
COPY php.ini /usr/local/etc/php/  
RUN apt-get update && apt-get install -y libssl-dev libmemcached-dev
zlib1g-dev libmcrypt-dev && rm -rf /var/lib/apt/lists/*  
RUN pecl install mongo-1.6.14 \  
&& pecl install memcached-2.2.0 \  
&& docker-php-ext-enable mongo memcached \  
&& docker-php-ext-install pdo pdo_mysql mcrypt \  
&& docker-php-ext-install zip \  

