FROM php:7.2-rc-fpm  
# copy from https://github.com/laradock/php-fpm/blob/master/Dockerfile-71  
MAINTAINER zcong1993 <zhangcong1992@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
libmemcached-dev \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng-dev \  
libfreetype6-dev \  
libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install the PHP pdo_mysql extention  
RUN docker-php-ext-install pdo_mysql \  
# Install the PHP pdo_pgsql extention  
&& docker-php-ext-install pdo_pgsql \  
# Install the PHP gd library  
&& docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
# Install the PHP memcached extention  
RUN curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-
dev/php-memcached/archive/php7.tar.gz" \  
&& mkdir -p memcached \  
&& tar -C memcached -zxvf /tmp/memcached.tar.gz --strip 1 \  
&& ( \  
cd memcached \  
&& phpize \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install \  
) \  
&& rm -r memcached \  
&& rm /tmp/memcached.tar.gz \  
&& docker-php-ext-enable memcached

