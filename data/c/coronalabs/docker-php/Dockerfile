FROM php:fpm  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=www-data --with-fpm-
group=www-data --enable-opcache  
  
# lumen packages  
RUN apt-get update \  
&& buildDeps=" \  
libmcrypt-dev \  
pkg-config \  
build-essential \  
libmemcached-dev \  
zlib1g-dev \  
" \  
&& apt-get install -y $buildDeps \  
&& apt-get install -y git zlib1g \  
&& docker-php-source extract \  
&& git clone https://github.com/php-memcached-dev/php-memcached.git \  
&& cd php-memcached \  
&& git checkout php7 \  
&& phpize \  
&& ./configure --disable-memcached-sasl \  
&& make \  
&& make install \  
&& docker-php-ext-enable memcached \  
&& docker-php-source delete \  
&& docker-php-ext-enable opcache \  
&& docker-php-ext-install -j$(nproc) mcrypt mbstring tokenizer mysqli \  
&& docker-php-ext-install sockets \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps  
RUN apt-get install libmcrypt4 libmemcached11 libmemcachedutil2  
COPY config/opcache.ini /usr/local/etc/opcache.ini  
RUN cat /usr/local/etc/opcache.ini >>/usr/local/etc/php/conf.d/docker-php-ext-
opcache.ini  
COPY config/*.conf /usr/local/etc/php-fpm.d/  
  
EXPOSE 9000 9001 9002  

