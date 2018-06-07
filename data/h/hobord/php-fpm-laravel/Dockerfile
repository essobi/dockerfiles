FROM php:7.2-fpm-stretch  
  
MAINTAINER Balazs Szabo <balazs.szabo@gmail.com>  
  
RUN apt-get update -yqq \  
&& buildDeps=" \  
libc-client2007e-dev \  
libjpeg62-turbo-dev \  
libpq-dev \  
libcurl4-openssl-dev \  
libjpeg-dev \  
libpng-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
libc-client-dev \  
libkrb5-dev \  
libxml2-dev \  
" \  
&& doNotUninstall=" \  
libc-client2007e \  
libmemcached11 \  
libmemcachedutil2 \  
libfreetype6 \  
libhashkit2 \  
libjpeg62-turbo \  
libmcrypt4 \  
libpq5 \  
" \  
&& apt-get install -y \  
apt-utils \  
curl \  
git \  
unzip \  
tar \  
less \  
$buildDeps \  
\--no-install-recommends \  
&& pecl install mcrypt-1.0.1 \  
&& docker-php-ext-enable mcrypt \  
&& docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 \  
&& docker-php-ext-configure imap \  
\--with-imap-ssl \  
\--with-kerberos \  
&& docker-php-ext-install \  
imap \  
pdo_mysql \  
mysqli \  
mbstring \  
gd \  
iconv \  
hash \  
sockets \  
dom \  
zip \  
xml \  
simplexml \  
xmlwriter \  
soap \  
json \  
exif \  
curl \  
&& pecl install redis \  
&& pecl install mongodb \  
&& docker-php-ext-enable redis \  
&& docker-php-ext-enable mongodb \  
&& pecl clear-cache \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& apt-get clean \  
&& apt-mark manual $doNotUninstall \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps \  
&& docker-php-source delete \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN usermod -u 1000 www-data  

