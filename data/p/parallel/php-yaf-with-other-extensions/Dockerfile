FROM php:7.0-fpm  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install pdo_mysql  
  
RUN pecl install yaf  
  
COPY yaf.ini /usr/local/etc/php/conf.d/yaf.ini  
  
RUN docker-php-ext-install pcntl shmop soap sockets wddx  
  
RUN pecl install redis \  
&& docker-php-ext-enable redis  
  
RUN apt-get install libcurl4-openssl-dev pkg-config -y  
  
RUN curl -fsSL 'http://pecl.php.net/get/stomp-2.0.0.tgz' -o stomp.tar.gz \  
&& mkdir -p stomp \  
&& tar -xf stomp.tar.gz -C stomp --strip-components=1 \  
&& rm stomp.tar.gz \  
&& ( \  
cd stomp \  
&& phpize \  
&& ./configure --enable-stomp \  
&& make \  
&& make install \  
) \  
&& rm -r stomp \  
&& docker-php-ext-enable stomp  
  
RUN pecl install zip \  
&& docker-php-ext-enable zip  
  
RUN pecl install xdebug  
  
COPY xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  

