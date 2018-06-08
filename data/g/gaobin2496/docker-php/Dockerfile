FROM php:apache  
MAINTAINER Bin Gao  
ENV PHPREDIS_VERSION=php7  
RUN cd /usr/src/php/ext \  
&& curl -q
https://codeload.github.com/phpredis/phpredis/tar.gz/$PHPREDIS_VERSION | tar
-xz \  
&& docker-php-ext-install phpredis-$PHPREDIS_VERSION  
RUN docker-php-ext-install pdo pdo_mysql  
RUN a2enmod rewrite  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
&& docker-php-ext-install -j$(nproc) mcrypt  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install bcmath  
  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
RUN sed -i '1 a xdebug.remote_autostart=true'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_connect_back=1 '
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_port=9000' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_host=192.168.1.159'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
EXPOSE 80 9000  

