FROM php:5.6-fpm  
  
MAINTAINER Berry Goudswaard <info@berrygoudswaard.nl>  
  
RUN apt-get update \  
&& apt-get install -y \  
g++ \  
git-core \  
libfreetype6-dev \  
libicu-dev libpng12-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
&& docker-php-ext-install mbstring intl pdo_mysql pdo_pgsql mcrypt iconv zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN git clone \--branch xdebug_2_3 git://github.com/xdebug/xdebug.git
/usr/src/php/ext/xdebug \  
&& cd /usr/src/php/ext/xdebug \  
&& phpize \  
&& ./configure --enable-xdebug \  
&& make \  
&& make install \  
&& echo 'zend_extension=/usr/src/php/ext/xdebug/modules/xdebug.so' >
/usr/local/etc/php/conf.d/ext-xdebug.ini  
  
CMD ["php-fpm"]  

