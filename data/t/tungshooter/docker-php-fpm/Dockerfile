FROM php:7.1-fpm  
  
MAINTAINER Tran Duc Thang <thangtd90@gmail.com>  
  
ENV TERM xterm  
  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
libmemcached-dev \  
curl \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
vim \  
zlib1g-dev libicu-dev g++ \  
\--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
# configure gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2  
  
# configure intl  
RUN docker-php-ext-configure intl  
  
# Install mongodb, xdebug  
RUN pecl install mongodb \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
# Install extensions using the helper script provided by the base image  
RUN docker-php-ext-install \  
mcrypt \  
bcmath \  
pdo_mysql \  
pdo_pgsql \  
gd \  
intl \  
zip  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www/html  
  
ADD ./website.ini /usr/local/etc/php/conf.d  
ADD ./website.pool.conf /usr/local/etc/php-fpm.d/  
  
CMD ["php-fpm"]  
  
EXPOSE 9000  

