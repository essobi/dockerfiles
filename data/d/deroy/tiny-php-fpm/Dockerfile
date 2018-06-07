FROM php:7.0-fpm  
  
MAINTAINER Roman Bulgakov  
LABEL version=1.0  
  
WORKDIR /root  
RUN buildDeps='git libicu-dev libmcrypt-dev libfreetype6-dev libjpeg-dev
libjpeg62-turbo-dev libpng12-dev zlib1g-dev libxml2-dev' && \  
set -x && \  
apt-get update && \  
apt-get -y install \  
g++ \  
libicu52 \  
libmcrypt4 \  
libfreetype6 \  
libjpeg62-turbo \  
libpng12-0 \  
zlib1g \  
libxml2 \  
mysql-client \  
openssh-client \  
$buildDeps \  
\--no-install-recommends && \  
# Install PHP extensions required for Yii 2.0 Framework  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/include/ && \  
docker-php-ext-configure bcmath && \  
docker-php-ext-install gd \  
intl \  
pdo_mysql \  
mbstring \  
mcrypt \  
zip \  
bcmath \  
soap && \  
# Install PECL extensions  
# see http://stackoverflow.com/a/8154466/291573) for usage of `printf`  
printf "\n" | pecl install apcu-5.1.3 xdebug-2.4.0 && \  
# clean the mess  
apt-get clean && \  
apt-get purge -y --auto-remove $buildDeps && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Configuration  
COPY ./container-files/php.ini /usr/local/etc/php/conf.d/

