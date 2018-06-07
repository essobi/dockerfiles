FROM php:7.1.5-apache  
  
RUN apt-get update && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev
libmcrypt-dev libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt && docker-php-ext-configure
gd \--with-freetype-dir=/usr/include/ \--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd zip mysqli pdo_mysql \  
&& cp /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/ \  
&& pecl install xdebug-2.5.0 && docker-php-ext-enable xdebug  

