#
================================================================================================================  
#  
# NGINX and PHP-FPM with plus some common extensions  
#  
# @see https://github.com/AlbanMontaigu/docker-nginx-php-plus  
#
================================================================================================================  
# Base is a nginx install with php  
FROM amontaigu/nginx-php:5.6.29  
# Maintainer  
MAINTAINER alban.montaigu@gmail.com  
  
# System update & install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends libpng12-dev libjpeg-dev
libfreetype6-dev libjpeg62-turbo-dev libgd2-xpm-dev libmagickwand-dev
imagemagick libmcrypt-dev \  
&& docker-php-ext-install mcrypt mbstring mysqli pdo_mysql zip gettext exif \  
&& pecl install imagick-beta \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-png-
dir=/usr/include/ \--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-enable gd \  
&& rm -rf /var/lib/apt/lists/* \  
# Install composer since more php apps require it  
&& curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  

