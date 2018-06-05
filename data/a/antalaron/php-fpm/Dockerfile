FROM php:7.1-fpm  
MAINTAINER Antal Áron <antalaron@antalaron.hu>  
  
ENV TZ=Europe/Budapest  
  
RUN apt-get update && \  
apt-get install -y \  
comerr-dev \  
krb5-multidev \  
libblkid1:amd64 \  
libc-client2007e-dev \  
libc-dev-bin \  
libc6-dev:amd64 \  
libcurl4-openssl-dev:amd64 \  
libdevmapper1.02.1:amd64 \  
libgcc-4.9-dev:amd64 \  
libjpeg-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libkrb5-dev \  
libmcrypt-dev \  
libmount1:amd64 \  
libpam0g-dev:amd64 \  
libpng12-dev:amd64 \  
libssl-dev:amd64 \  
libssl-doc \  
libicu-dev \  
libstdc++-4.9-dev:amd64 \  
libudev1:amd64 \  
linux-libc-dev:amd64 \  
libmemcached-dev \  
libxml2-dev \  
zlib1g-dev:amd64 \  
unzip \  
zip \  
git && \  
\  
rm -rf /var/lib/apt/lists/* && \  
\  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install \  
curl \  
gd \  
iconv \  
mcrypt \  
hash \  
mysqli \  
pdo \  
pdo_mysql \  
imap \  
ftp \  
session \  
pdo_mysql \  
exif \  
simplexml \  
zip \  
ctype \  
mbstring \  
intl \  
bcmath \  
opcache && \  
\  
cp /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo "Europe/Budapest" > /etc/timezone && \  
echo "expose_php=Off" > $PHP_INI_DIR/conf.d/docker-php.ini && \  
echo "memory_limit=4G" >> $PHP_INI_DIR/conf.d/docker-php.ini && \  
echo "max_execution_time=900" >> $PHP_INI_DIR/conf.d/docker-php.ini && \  
echo "timezone=$TZ" >> $PHP_INI_DIR/conf.d/docker-php.ini && \  
echo "upload_max_filesize=2G" >> $PHP_INI_DIR/conf.d/docker-php.ini && \  
echo "post_max_size=2G" >> $PHP_INI_DIR/conf.d/docker-php.ini && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

