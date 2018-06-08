FROM phalconphp/php-fpm:7.1-min  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt pdo pdo_mysql soap \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
RUN php -m  

