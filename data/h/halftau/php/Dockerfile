FROM php:fpm-alpine  
  
MAINTAINER Pablo Perich "pablo.perich@halftau.com"  
  
COPY www-php-ini.conf /usr/local/etc/php-fpm.d/  
  
RUN chmod 622 /usr/local/etc/php-fpm.d/* && \  
  
apk add \  
re2c \  
libpq \  
gettext-libs \  
icu-libs \  
\--update && \  
  
apk add \  
file \  
binutils \  
coreutils \  
g++ \  
make \  
autoconf \  
wget \  
gettext-dev \  
postgresql-dev \  
icu-dev \  
\--virtual devpacks && \  
  
cd /tmp && \  
wget https://github.com/websupport-sk/pecl-
memcache/archive/NON_BLOCKING_IO_php7.zip -O pecl-memcache-
NON_BLOCKING_IO_php7.zip && \  
unzip pecl-memcache-NON_BLOCKING_IO_php7.zip && \  
cd pecl-memcache-NON_BLOCKING_IO_php7 && \  
phpize && \  
./configure && \  
make && \  
make install && \  
cd /tmp && \  
rm -rf * && \  
docker-php-ext-enable memcache && \  
  
cd /tmp && \  
wget https://github.com/krakjoe/apcu/archive/v5.1.5.zip -O apcu-5.1.5.zip && \  
unzip apcu-5.1.5.zip && \  
cd apcu-5.1.5 && \  
phpize && \  
./configure && \  
make && \  
make install && \  
cd /tmp && \  
rm -rf * && \  
docker-php-ext-enable apcu && \  
  
docker-php-ext-enable opcache && \  
  
docker-php-ext-install -j$(nproc) intl pcntl zip gettext pdo_pgsql sockets &&
\  
  
apk del devpacks --purge && \  
  
mkdir -p /var/lib/halftau/persist && \  
chown www-data /var/lib/halftau/persist && \  
chgrp www-data /var/lib/halftau/persist && \  
mkdir -p /var/lib/halftau/root  
  
VOLUME /var/lib/halftau/persist  

