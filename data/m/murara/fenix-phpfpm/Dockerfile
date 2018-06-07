FROM php:5.5-fpm  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install sockets \  
&& docker-php-ext-install zip \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY config/php.ini /usr/local/etc/php/php.ini  
COPY config/php-fpm.conf /usr/local/etc/php-fpm.conf  

