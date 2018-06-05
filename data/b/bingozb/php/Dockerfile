FROM php:5.6-fpm-alpine  
MAINTAINER bingo <bingov5@icloud.com>  
  
# usermod www-data  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories \  
&& apk --no-cache add shadow && usermod -u 1000 www-data  
  
# timezone  
ENV TIMEZONE Asia/Shanghai  
RUN apk add --no-cache tzdata \  
&& ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime \  
&& echo $TIMEZONE > /etc/timezone  
  
# mbstring opcache pdo mysql  
RUN docker-php-ext-install mbstring opcache pdo pdo_mysql mysql mysqli  
  
# gd zip  
RUN apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev
libjpeg-turbo-dev \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir \  
\--with-png-dir \  
\--with-jpeg-dir \  
\--with-zlib-dir \  
&& docker-php-ext-install -j${NPROC} gd zip \  
&& apk del freetype-dev libpng-dev libjpeg-turbo-dev  
  
# redis  
ENV PHPREDIS_VERSION 4.0.0RC1  
RUN apk add --no-cache curl \  
&& curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mkdir -p /usr/src/php/ext \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install redis \  
&& rm -rf /usr/src/php \  
&& apk del curl

