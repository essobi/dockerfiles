FROM php:7.0.3-fpm  
  
RUN apt-get update && apt-get install -y --no-install-recommends git
libpng12-dev zlib1g-dev libicu-dev g++ libjpeg-dev libpq-dev libmemcached11
libmemcached-dev libmcrypt-dev libfreetype6-dev libgd-dev openssl libc-client-
dev libkrb5-dev libbz2-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr
\--with-freetype-dir=/usr \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& mkdir -p /usr/src/php/ext/memcached && git clone -b php7
https://github.com/php-memcached-dev/php-memcached.git
/usr/src/php/ext/memcached \  
&& mkdir -p /usr/src/php/ext/redis && git clone -b php7
https://github.com/phpredis/phpredis.git /usr/src/php/ext/redis \  
&& docker-php-ext-install bz2 calendar gd mbstring memcached imap mcrypt exif
intl opcache redis pdo pdo_mysql pdo_pgsql ftp zip  

