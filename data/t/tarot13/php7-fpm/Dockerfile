FROM php:fpm-alpine3.7  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
RUN apk add --no-cache bash musl nano cyrus-sasl libmemcached freetype
libjpeg-turbo libpng libwebp libxpm \  
tzdata autoconf g++ make libmemcached-dev cyrus-sasl-dev libjpeg-turbo-dev
libwebp-dev libpng-dev freetype-dev libxpm-dev && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
docker-php-source extract && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install exif mysqli opcache pdo_mysql sockets tokenizer zip gd
&& \  
pecl install -o -f igbinary redis memcached && \  
docker-php-ext-enable igbinary redis memcached && \  
docker-php-source delete && \  
apk del tzdata autoconf g++ make libmemcached-dev cyrus-sasl-dev libjpeg-
turbo-dev libwebp-dev libpng-dev freetype-dev libxpm-dev && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer

