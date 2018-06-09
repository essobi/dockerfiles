# https://github.com/jwilder/nginx-proxy  
FROM php:alpine  
  
# 作成者情報  
MAINTAINER toshi <toshi@toshi.click>  
  
RUN apk --update upgrade && \  
apk add autoconf \  
automake \  
make \  
postgresql-client \  
postgresql-dev \  
gcc \  
g++ \  
libtool \  
pkgconfig \  
libmcrypt-dev \  
re2c \  
git \  
zlib-dev \  
xdg-utils \  
libpng-dev \  
freetype-dev \  
libjpeg-turbo-dev \  
openssh-client \  
libxslt-dev \  
ca-certificates \  
gmp-dev  
  
RUN docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/  
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql  
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null ||
1) gd pgsql pdo pdo_pgsql mysqli pdo_mysql bcmath zip json iconv fileinfo
sockets  
RUN pecl install mailparse && \  
docker-php-ext-enable mailparse  

