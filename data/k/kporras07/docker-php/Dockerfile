FROM php:7-fpm-alpine  
  
ENV XDEBUG_VERSION 2.3.3  
RUN docker-php-source extract \  
&& apk --no-cache --update add \  
libxml2-dev \  
libpng \  
libpng-dev \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
freetype-dev \  
freetype \  
curl \  
icu-dev \  
g++ \  
autoconf \  
make \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/* \  
&& docker-php-ext-configure bcmath \  
&& docker-php-ext-configure json \  
&& docker-php-ext-configure session \  
&& docker-php-ext-configure ctype \  
&& docker-php-ext-configure tokenizer \  
&& docker-php-ext-configure simplexml \  
&& docker-php-ext-configure dom \  
&& docker-php-ext-configure mbstring \  
&& docker-php-ext-configure zip \  
&& docker-php-ext-configure iconv \  
&& docker-php-ext-configure xml \  
&& docker-php-ext-configure opcache \  
&& docker-php-ext-configure pdo \  
&& docker-php-ext-configure pdo_mysql \  
&& docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-install -j${NPROC} gd \  
&& docker-php-source delete  
  
RUN docker-php-ext-install bcmath \  
json \  
session \  
ctype \  
tokenizer \  
simplexml \  
dom \  
mbstring \  
zip \  
iconv \  
xml \  
opcache \  
pdo \  
pdo_mysql  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
  
# Cleanup  
RUN rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf tmp/*  
  
# Xdebug settings.  
COPY ./xdebug.ini /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  

