FROM php:7.1-fpm  
  
MAINTAINER Deon Thomas "Deon.Thomas.GY@gmail.com"  
#refresh  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmagickwand-6.q16-dev \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& docker-php-ext-install iconv mcrypt pdo_mysql bcmath exif \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd zip  
  
RUN echo "php_value[memory_limit] = 512M" >> /usr/local/etc/php-fpm.conf  
RUN echo "php_value[date.timezone] = America/Guyana" >> /usr/local/etc/php-
fpm.conf  
  
CMD ["php-fpm"]  

