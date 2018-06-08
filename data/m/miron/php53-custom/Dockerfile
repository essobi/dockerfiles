FROM andthensome/docker-php-5.3-fpm  
MAINTAINER miron.ogrodowicz@kreativrudel.de  
  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libjpeg-dev \  
libpng12-dev \  
libpng-dev \  
libssl-dev \  
libicu-dev \  
libfreetype6-dev \  
libmcrypt-dev \  
; \  
rm -rf /var/lib/apt/lists/*; \  
mkdir -p /usr/include/freetype2/freetype; \  
ln -s /usr/include/freetype2/freetype.h
/usr/include/freetype2/freetype/freetype.h; \  
\  
docker-php-ext-install bcmath mbstring iconv mcrypt; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr --enable-
gd-native-ttf --with-freetype-dir=/usr/include/freetype2/freetype; \  
\  
docker-php-ext-install gd; \  
\  
pecl install phar; \  
docker-php-ext-install phar; \  
\  
pecl install intl; \  
docker-php-ext-install intl  
  
EXPOSE 9000

