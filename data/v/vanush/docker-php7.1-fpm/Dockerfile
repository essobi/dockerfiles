FROM php:7.1-fpm  
MAINTAINER Tom Sacré <github@digitalkreativ.com>  
  
# PHP config  
ADD ./php.ini /usr/local/etc/php/  
# Install modules  
RUN apt-get update \  
&& apt-get install -y \  
apt-utils \  
curl \  
dnsutils \  
git \  
unzip \  
wget \  
zip \  
libcurl4-gnutls-dev \  
libmcrypt-dev \  
libtidy-dev \  
libbz2-dev \  
libxml2-dev \  
libjpeg-dev \  
libfreetype6-dev \  
libjpeg62 \  
libpng-dev \  
libssl-dev \  
libicu-dev \  
libc-client-dev \  
libkrb5-dev \  
jpegoptim \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install \  
bcmath \  
bz2 \  
calendar \  
curl \  
exif \  
ftp \  
gd \  
gettext \  
imap \  
intl \  
json \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
pdo \  
pdo_mysql \  
shmop \  
soap \  
sockets \  
sysvmsg \  
sysvsem \  
sysvshm \  
tidy \  
wddx \  
zip  
  
# Possible values for ext-name:  
# bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter ftp gd
gettext gmp hash iconv imap  
# interbase intl json ldap mbstring mcrypt mysqli oci8 odbc opcache pcntl pdo
pdo_dblib pdo_firebird pdo_mysql  
# pdo_oci pdo_odbc pdo_pgsql pdo_sqlite pgsql phar posix pspell readline
recode reflection session shmop simplexml  
# snmp soap sockets spl standard sysvmsg sysvsem sysvshm tidy tokenizer wddx
xml xmlreader xmlrpc xmlwriter xsl zip  
  
WORKDIR /var/www/  
  
CMD php-fpm  
  

