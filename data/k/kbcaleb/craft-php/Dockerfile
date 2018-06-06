FROM php:7-fpm  
MAINTAINER Caleb Collins <kbcaleb@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
libmagickwand-6.q16-dev --no-install-recommends \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin \  
&& pecl install imagick-beta \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmcrypt-dev \  
zlib1g-dev \  
&& docker-php-ext-install -j$(nproc) pdo_mysql mbstring zip mcrypt \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
RUN chown -R www-data:www-data /var/www  

