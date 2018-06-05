FROM php:7.1-apache  
COPY php.ini /usr/local/etc/php/conf.d/  
ENV PHPREDIS_VERSION="php7"  
RUN apt-get update \  
&& apt-get install -y libmcrypt-dev libpng12-dev libfreetype6 libjpeg-dev
libfreetype6-dev golang-openldap-dev libxml2 libxml2-dev bzip2 libicu-dev
gettext libintl-perl libbz2-1.0 \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" gd gettext soap
opcache mcrypt mysqli pdo_mysql bcmath calendar exif pcntl shmop sysvsem dba
sockets wddx xmlrpc zip

