FROM php:7.2-cli  
  
MAINTAINER Dmitry Momot <mail@dmomot.com>  
  
ENV TERM xterm  
  
RUN apt-get update && apt-get install -y --force-yes \  
libpq-dev \  
curl \  
libjpeg-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
vim \  
cron \  
\--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
# install memcache extension  
RUN apt-get update \  
&& apt-get install -y libmemcached11 libmemcachedutil2 build-essential
libmemcached-dev libz-dev \  
&& pecl install memcached \  
&& echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini \  
&& apt-get remove -y build-essential libmemcached-dev libz-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/pear  
  
# configure gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2  
  
# Install mongodb, xdebug  
RUN pecl install mongodb \  
&& pecl install xdebug \  
&& docker-php-ext-enable mongodb xdebug  
  
# Install extensions using the helper script provided by the base image  
RUN docker-php-ext-install \  
bcmath \  
pdo_mysql \  
pdo_pgsql \  
gd \  
zip  
  
RUN pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable redis  
  
RUN usermod -u 1000 www-data  
  
ENV EDITOR vi  
  
WORKDIR /var/www/laravel  
  
ADD ./laravel.ini /usr/local/etc/php/conf.d  
ADD ./laravel.pool.conf /usr/local/etc/php-fpm.d/  
  
ENTRYPOINT ["docker-php-entrypoint", "php", "artisan"]  
CMD ["env"]  

