FROM php:5.6-fpm-alpine  
  
RUN apk update && \  
apk add php5-intl php5-gd php5-imagick \  
freetype libpng libjpeg-turbo freetype-dev \  
libpng-dev libjpeg-turbo-dev libmcrypt-dev && \  
# apk add php5-geoip  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
docker-php-ext-install -j${NPROC} gd zip mcrypt pdo_mysql && \  
apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev  
  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories  
RUN apk --no-cache add shadow && usermod -u 1000 www-data  
  
WORKDIR /usr/local/apache2/htdocs  

