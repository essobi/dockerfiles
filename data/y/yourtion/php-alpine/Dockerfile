FROM php:alpine  
  
RUN apk --no-cache add autoconf build-base freetype libpng libjpeg-turbo
freetype-dev libpng-dev libjpeg-turbo-dev libmcrypt-dev && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
docker-php-ext-install -j${NPROC} iconv mcrypt gd mysqli pdo pdo_mysql && \  
pecl install -o -f redis && \  
docker-php-ext-enable redis && \  
apk del autoconf build-base  
  
ENTRYPOINT ["php"]  

