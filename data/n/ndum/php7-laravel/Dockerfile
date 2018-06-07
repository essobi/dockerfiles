FROM php:7-fpm  
LABEL authors="Nicolas D. <nd@nidum.org> / Simon Baerlocher
<s.baerlocher@sbaerlocher.ch>"  
# Install all required packages.  
RUN apt-get update && \  
apt-get install \  
git \  
libldap2-dev \  
libcurl4-gnutls-dev \  
curl \  
libicu-dev \  
libmcrypt-dev \  
libvpx-dev \  
libjpeg-dev \  
libpng-dev \  
libxpm-dev \  
zlib1g-dev \  
libfreetype6-dev \  
libxml2-dev \  
libexpat1-dev \  
libbz2-dev \  
libgmp3-dev \  
libldap2-dev \  
unixodbc-dev \  
libpq-dev \  
libsqlite3-dev \  
libaspell-dev \  
libsnmp-dev \  
libpcre3-dev \  
libtidy-dev \  
build-essential \  
libkrb5-dev \  
libedit-dev \  
libedit2 \  
gcc \  
make \  
python2.7-dev \  
python-pip \  
re2c \  
wget \  
sqlite3 \  
libmemcached-dev \  
libc-client-dev -yqq \  
&& rm -rf /var/lib/apt/lists/*  
  
# Compile PHP, include these extensions.  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/  
RUN docker-php-ext-configure imap --with-imap-ssl --with-kerberos --with-imap  
RUN docker-php-ext-install mbstring \  
pdo_mysql \  
json \  
intl \  
gd \  
xml \  
zip \  
bz2 \  
opcache \  
pgsql \  
pdo_sqlite\  
intl \  
bcmath \  
soap \  
ldap \  
imap \  
readline  
  
# Compile and install APCu  
RUN pecl install apcu \  
&& docker-php-ext-enable apcu  
  
#install Imagemagick & PHP Imagick ext  
RUN apt-get update && apt-get install -y \  
libmagickwand-dev --no-install-recommends  
RUN pecl install imagick && docker-php-ext-enable imagick  
  
# Removed xDebug temporally, non source version is incompatible with PHP
7.2-RC  
# Compile and install xDebug  
# RUN pecl install xdebug \  
# && docker-php-ext-enable xdebug  
# Deploy improved php.ini  
COPY conf/php.ini /usr/local/etc/php/php.ini  
  
# Add user 1000 to www-data  
RUN usermod -u 1000 www-data  
  
CMD ["php-fpm"]

