FROM php:7.1-apache  
RUN usermod -u 1000 www-data  
RUN a2enmod rewrite  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libicu-dev \  
libpng12-dev \  
libssl-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install -j$(nproc) pdo \  
&& docker-php-ext-install -j$(nproc) pdo_mysql \  
&& docker-php-ext-install -j$(nproc) intl \  
&& docker-php-ext-install -j$(nproc) mysqli \  
&& docker-php-ext-install -j$(nproc) mbstring \  
&& docker-php-ext-install -j$(nproc) ftp \  
&& docker-php-ext-install -j$(nproc) zip  
  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
COPY ./extensions.ini /usr/local/etc/php/conf.d/extensions.ini  

