FROM php:7-fpm-alpine  
RUN apk add --no-cache freetype libpng libjpeg-turbo && \  
apk add --no-cache --virtual .build-dependencies libpng-dev libmcrypt-dev
libxml2-dev freetype-dev libpng-dev libjpeg-turbo-dev icu-dev curl-dev
gettext-dev  
  
  
# Possible values for ext-name:  
# bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter ftp gd
gettext gmp hash iconv imap interbase intl  
# json ldap mbstring mcrypt mssql mysql mysqli oci8 odbc opcache pcntl pdo
pdo_dblib pdo_firebird pdo_mysql pdo_oci  
# pdo_odbc pdo_pgsql pdo_sqlite pgsql phar posix pspell readline recode
reflection session shmop simplexml snmp soap  
# sockets spl standard sybase_ct sysvmsg sysvsem sysvshm tidy tokenizer wddx
xml xmlreader xmlrpc xmlwriter xsl zip  
  
  
RUN docker-php-ext-configure intl --enable-intl && \  
docker-php-ext-configure mbstring --enable-mbstring && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
docker-php-ext-install \  
gettext \  
hash \  
xml \  
fileinfo \  
ftp \  
simplexml \  
ctype \  
iconv \  
json \  
curl \  
intl \  
mbstring \  
pdo_mysql \  
calendar \  
opcache \  
mcrypt \  
soap \  
zip \  
mysqli && \  
docker-php-ext-install -j${NPROC} gd  
  
RUN apk del .build-dependencies  

