FROM php:7.0-fpm  
MAINTAINER Stayfi B. <stayfi@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libsqlite3-dev \  
libssl-dev \  
libcurl3-dev \  
libxml2-dev \  
libzzip-dev \  
ssmtp \  
libicu-dev \  
g++ \  
&& docker-php-ext-install iconv json mcrypt mbstring mysqli pdo_mysql
pdo_sqlite phar curl ftp hash session simplexml tokenizer xml xmlrpc zip intl
\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& sed -i '1 a xdebug.remote_autostart=true' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_connect_back=1 '
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_port=9001' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]

