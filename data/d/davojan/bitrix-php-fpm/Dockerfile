FROM php:7.0-fpm  
  
MAINTAINER davojan  
  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
libmemcached-dev \  
curl \  
wget \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
\--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
# install mcrypt library  
RUN docker-php-ext-install mcrypt  
  
# configure gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2  
  
# Install extensions using the helper script provided by the base image  
RUN docker-php-ext-install \  
opcache \  
mysqli \  
gd  
  
RUN wget https://github.com/websupport-sk/pecl-
memcache/archive/NON_BLOCKING_IO_php7.tar.gz \  
&& tar -zxvf NON_BLOCKING_IO_php7.tar.gz \  
&& cd pecl-memcache-NON_BLOCKING_IO_php7 \  
&& phpize && ./configure --enable-memcache && make \  
&& cp modules/memcache.so /usr/local/lib/php/extensions/no-debug-non-
zts-20151012/ \  
&& docker-php-ext-enable memcache \  
&& rm -rf NON_BLOCKING_IO_php7.zip \  
&& rm -rf pecl-memcache-NON_BLOCKING_IO_php7  
  
# Install xdebug  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
ADD ./bitrix.ini /usr/local/etc/php/conf.d/  
ADD ./laravel.pool.conf /usr/local/etc/php-fpm.d/  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www/site  
  
CMD ["php-fpm"]  
  
EXPOSE 9000  

