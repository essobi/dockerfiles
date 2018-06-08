FROM php:5.6-fpm  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl3-dev \  
zlib1g-dev \  
git \  
libz-dev libmemcached-dev  
  
RUN docker-php-ext-install pdo pdo_mysql curl pcntl opcache \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt zip tokenizer \  
&& docker-php-ext-enable pcntl \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN pecl install memcached-2.2.0 \  
&& echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini \  
&& apt-get remove -y build-essential libmemcached-dev libz-dev  
  
  
COPY composer-install.sh composer-install.sh  
  
RUN apt-get install -y wget && \  
chmod +x composer-install.sh && ./composer-install.sh && rm -f composer-
install.sh && \  
mv composer.phar /usr/bin/composer && chmod +x /usr/bin/composer && \  
apt-get remove -y wget  
  
WORKDIR /var/www

