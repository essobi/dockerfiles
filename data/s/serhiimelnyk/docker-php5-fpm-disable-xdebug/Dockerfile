FROM php:5.6-fpm  
  
COPY php.ini /usr/local/etc/php/php.ini  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
php5-dev \  
php5-mysql \  
php5-sqlite \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& pecl install mongo \  
&& docker-php-ext-enable mongo \  
&& docker-php-ext-install exif \  
&& docker-php-ext-install pdo pdo_mysql \  
&& docker-php-ext-install -j$(nproc) intl  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]  

