FROM php:7.2-fpm-alpine  
  
LABEL maintainer="mingpeng16@gmail.com"  
# ENV PHPIZE_DEPS  
  
ARG ALPINE_URL=dl-cdn.alpinelinux.org  
  
# Add timezone support  
# --no-cache: This avoids the need to use --update and remove /var/cache/apk/*
when done installing packages.  
RUN sed -i "s:dl-cdn.alpinelinux.org:${ALPINE_URL}:g" /etc/apk/repositories \  
&& apk add --no-cache tzdata \  
freetype \  
libjpeg-turbo \  
libpng \  
&& apk add --no-cache --virtual .build-deps \  
# $PHPIZE_DEPS \  
# libmcrypt-dev \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-install -j${NPROC} \  
# mcrypt \  
mysqli \  
pdo_mysql \  
zip \  
opcache \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-install -j${NPROC} gd \  
&& apk del .build-deps \  
&& rm -rf /tmp/*  
  
ARG TZ  
  
ENV TZ ${TZ:-UTC}

