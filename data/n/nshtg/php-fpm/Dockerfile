FROM php:7.2.3-fpm-alpine3.7  
  
RUN deluser xfs \  
&& deluser www-data \  
&& addgroup -g 33 -S www-data \  
&& adduser -u 33 -D -S -h /var/cache/www-data -s /sbin/nologin -G www-data
www-data \  
&& apk add --no-cache --update \  
libxml2-dev \  
sqlite-dev \  
curl-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
freetype-dev \  
&& apk add libsodium-dev --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/main \  
&& rm -rf /var/cache/apk \  
&& docker-php-ext-configure ctype \  
&& docker-php-ext-configure curl \  
&& docker-php-ext-configure dom \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include \  
&& docker-php-ext-configure iconv \  
&& docker-php-ext-configure json \  
&& docker-php-ext-configure mbstring \  
&& docker-php-ext-configure mysqli \  
&& docker-php-ext-configure pdo \  
&& docker-php-ext-configure pdo_mysql \  
&& docker-php-ext-configure pdo_sqlite \  
&& docker-php-ext-configure session \  
&& docker-php-ext-configure simplexml \  
&& docker-php-ext-configure sodium \  
&& docker-php-ext-configure tokenizer \  
&& docker-php-ext-configure xml \  
&& docker-php-ext-configure zip \  
&& docker-php-ext-install ctype \  
curl \  
dom \  
gd \  
iconv \  
json \  
mbstring \  
mysqli \  
pdo \  
pdo_mysql \  
pdo_sqlite \  
session \  
simplexml \  
sodium \  
tokenizer \  
xml \  
zip  
  
COPY rootfs /  
  
EXPOSE 9000  
  
CMD ["php-fpm", "-F"]  

