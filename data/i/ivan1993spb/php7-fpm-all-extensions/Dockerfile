  
FROM php:7.1-rc-fpm  
  
MAINTAINER Ivan Pushkin <iv.pushk@gmail.com>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
libbz2-dev \  
libc-client2007e-dev \  
libcurl4-gnutls-dev \  
libedit-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libkrb5-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libsqlite3-dev \  
libxml2-dev \  
libxslt1-dev \  
php-pear  
  
RUN mkdir -p /usr/kerberos  
RUN ln -s /usr/lib/x86_64-linux-gnu /usr/kerberos/lib  
  
RUN docker-php-ext-install -j$(nproc) \  
bz2 \  
curl \  
exif \  
iconv \  
intl \  
json \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
pdo_sqlite \  
pgsql \  
readline \  
soap \  
xml \  
xmlrpc \  
xsl \  
zip  
  
RUN docker-php-ext-configure imap --with-kerberos=/usr/kerberos --with-imap-
ssl \  
&& docker-php-ext-install -j$(nproc) imap  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN rm -rf /var/www/*  
RUN echo "<?php phpinfo();" > /var/www/index.php  
  
WORKDIR /var/www  

