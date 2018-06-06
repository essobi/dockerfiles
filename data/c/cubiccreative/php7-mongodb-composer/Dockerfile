FROM php:7.0.4-fpm  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libssl-dev \  
&& pecl install mongodb \  
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/ext-mongodb.ini \  
&& echo "upload_max_filesize = 5M" > /usr/local/etc/php/conf.d/upload.ini \  
&& docker-php-ext-install iconv mcrypt mbstring exif zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
  
WORKDIR /usr/share/nginx/html/Bitdin-Core  

