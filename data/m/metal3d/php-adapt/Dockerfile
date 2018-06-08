FROM php:7-apache  
RUN set -xe; \  
apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev; \  
docker-php-ext-install -j$(nproc) iconv mcrypt; \  
docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/; \  
docker-php-ext-install -j$(nproc) gd; \  
docker-php-ext-install mysqli;  
  
# adapt userid and groupid  
ONBUILD ARG WWW_UID  
ONBUILD ARG WWW_GID  
ONBUILD RUN usermod -u $WWW_UID www-data; groupmod -g $WWW_GID www-data;  

