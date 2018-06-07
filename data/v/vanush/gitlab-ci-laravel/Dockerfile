FROM php:7.1  
MAINTAINER Vanush Ghamaryan <vanush.kamaryan@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
git \  
libcurl4-gnutls-dev \  
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
python-software-properties \  
zip unzip\  
ntfs-3g\  
cifs-utils \  
mysql-client \  
&& docker-php-ext-install mbstring mcrypt pdo_mysql curl json intl gd xml zip
bz2 opcache soap tidy \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
&& pecl install mongodb \  
&& docker-php-ext-enable mongodb\  
&& pecl install mailparse \  
&& docker-php-ext-enable mailparse\  
&& cd ~ \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install nodejs  

