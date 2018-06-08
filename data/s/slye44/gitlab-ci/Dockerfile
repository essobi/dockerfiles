FROM php:7.1  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
git \  
curl \  
libmemcached-dev \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng-dev \  
libfreetype6-dev \  
libssl-dev \  
zlib1g-dev  
  
COPY conf/php.ini /usr/local/etc/php/  
  
RUN yes | pecl install xdebug  
RUN docker-php-ext-enable xdebug  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install zip  
  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  

