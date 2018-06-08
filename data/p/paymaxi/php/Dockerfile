FROM php:7.1-fpm  
  
ENV TERM=xterm  
  
ENV PHPIZE_DEPS \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c  
  
ENV PHPEXT_DEPS \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
zlib1g-dev \  
libicu-dev \  
re2c  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
$PHPEXT_DEPS \  
git \  
sudo \  
unzip \  
supervisor \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mbstring pcntl pdo pdo_pgsql
pgsql intl opcache zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd bcmath \  
&& pecl install apcu \  
&& cd /tmp && git clone https://github.com/xdebug/xdebug.git && cd xdebug &&
phpize && ./configure && make && make install  
  
RUN apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $PHPIZE_DEPS \  
&& rm /tmp/* -rf \  
&& rm /var/cache/apt/* -rf \  
&& rm /usr/src/php -rf \  
&& rm /usr/share/doc -rf \  
&& rm /usr/share/man -rf  
  
RUN curl -s https://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer  

