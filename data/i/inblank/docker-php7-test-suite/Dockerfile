FROM php:7.0-cli  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmemcached-dev \  
libicu-dev \  
libpq5 \  
libpq-dev \  
&& docker-php-ext-install -j$(nproc) pdo_mysql mcrypt intl zip pdo_pgsql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached \  
&& apt-get remove libpq-dev -y \  
&& apt-get autoremove -y  

