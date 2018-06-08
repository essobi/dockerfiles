FROM php:7.1.15-fpm  
MAINTAINER miron.ogrodowicz@kreativrudel.de  
  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libjpeg-dev \  
libpng12-dev \  
libssl-dev \  
libicu-dev \  
libfreetype6-dev \  
libxml2-dev \  
libmagickwand-dev \  
imagemagick \  
; \  
  
pecl install imagick; \  
docker-php-ext-enable imagick; \  
rm -rf /var/lib/apt/lists/*; \  
mkdir -p /usr/include/freetype2/freetype; \  
apt-get remove -y libmagickwand-dev; \  
ln -s /usr/include/freetype2/freetype.h
/usr/include/freetype2/freetype/freetype.h; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-
freetype-dir=/usr/include/freetype2/freetype; \  
docker-php-ext-install gd mysqli opcache soap zip phar intl; \  
\  
pecl install xdebug; \  
docker-php-ext-enable xdebug;  
  
EXPOSE 9000  

