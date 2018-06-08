FROM php:5.6-fpm  
  
MAINTAINER Deon Thomas "Deon.Thomas.GY@gmail.com"  
#refresh  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmagickwand-6.q16-dev \  
ca-certificates \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin \  
&& pecl install imagick xdebug-2.5.5 \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& docker-php-ext-install iconv mcrypt pdo_mysql bcmath exif \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd zip \  
&& php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ \--filename=composer  
CMD ["php-fpm"]  

