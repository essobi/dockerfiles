FROM php:7-fpm  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libpq-dev \  
g++ \  
libicu-dev \  
libxml2-dev \  
git \  
nano \  
libmemcached-dev \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install mysqli \  
  
&& apt-get purge --auto-remove -y g++ \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PHPREDIS_VERSION php7  
  
RUN curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& mkdir /tmp/redis \  
&& tar -xf /tmp/redis.tar.gz -C /tmp/redis \  
&& rm /tmp/redis.tar.gz \  
&& ( \  
cd /tmp/redis/phpredis-$PHPREDIS_VERSION \  
&& phpize \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install \  
) \  
&& rm -r /tmp/redis \  
&& docker-php-ext-enable redis  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
  
RUN pecl install apcu \  
&& docker-php-ext-enable apcu  
  
#install Imagemagick & PHP Imagick ext  
RUN apt-get update && apt-get install -y \  
libmagickwand-dev --no-install-recommends  
  
RUN pecl install imagick && docker-php-ext-enable imagick  
  
# TODO: review memcache integration  
#RUN apt-get update && apt-get install -y libmemcached-dev \  
# && pecl install memcached \  
# && docker-php-ext-enable memcached  
# install git  
RUN apt-get update && apt-get install git git-core -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
#install xdebugy  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
  
RUN sed -i -e 's/listen.*/listen = 0.0.0.0:9000/' /usr/local/etc/php-fpm.conf  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# remove unnecessary files  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]  
  
  
  

