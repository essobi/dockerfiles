FROM php:7.1-fpm  
ENV APT_LISTCHANGES_FRONTEND mail  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y -o DPkg::options::='--force-confdef'
-o Dpkg::Options::='--force-confold' \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
imagemagick \  
libgraphicsmagick1-dev \  
libmagickwand-dev \  
libcurl3 \  
curl \  
libcurl4-gnutls-dev \  
libicu-dev \  
libc-client2007e-dev \  
libc-client2007e \  
libkrb5-dev \  
libmysqlclient-dev \  
libzip-dev \  
libexif-dev \  
libmemcached-dev \  
libgmp-dev \  
libgmp3-dev \  
git \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& curl --output composer -Ss
https://getcomposer.org/download/1.2.0/composer.phar \  
&& mv composer /usr/bin/composer \  
&& chmod 755 /usr/bin/composer \  
&& chown root:root /usr/bin/composer \  
&& rm /usr/local/etc/php-fpm.d/www.conf /usr/local/etc/php-
fpm.d/www.conf.default  
RUN git clone https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached \  
&& cd /usr/src/php/ext/memcached \  
&& git checkout -b php7 origin/php7 \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install -j$(nproc) memcached  
RUN docker-php-ext-install -j$(nproc) bz2 fileinfo gmp mbstring opcache
pdo_mysql mysqli zip iconv mcrypt intl curl exif \  
&& pecl install imagick APCu \  
&& docker-php-ext-enable imagick apcu \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install -j$(nproc) gd imap  
RUN git clone https://github.com/websupport-sk/pecl-memcache
/usr/src/php/ext/memcache \  
&& cd /usr/src/php/ext/memcache \  
&& git checkout NON_BLOCKING_IO_php7 \  
&& docker-php-ext-configure memcache \  
&& docker-php-ext-install -j$(nproc) memcache  

