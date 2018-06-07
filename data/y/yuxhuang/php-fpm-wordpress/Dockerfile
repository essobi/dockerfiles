FROM php:7-fpm-alpine  
  
ARG PHPCONF=/usr/local/etc/php/conf.d  
  
ENV EUID 11000  
ENV EGID 21000  
  
RUN \  
build_pkgs="build-base autoconf automake libmemcached-dev imagemagick-dev
libtool zlib-dev cyrus-sasl-dev readline-dev libxml2-dev gd-dev curl-dev gmp-
dev libpng-dev freetype-dev zlib-dev libxpm-dev libwebp-dev" \  
&& runtime_pkgs="libmemcached libgcc imagemagick libltdl readline libxml2 gd
curl gmp libpng libjpeg freetype zlib libxpm libwebp libstdc++" \  
&& apk --no-cache add ${build_pkgs} ${runtime_pkgs} \  
&& docker-php-ext-install xmlrpc curl gd gmp json mysqli opcache pdo pdo_mysql
readline xmlrpc \  
&& yes | pecl install -sal imagick \  
&& mkdir -p /tmp/memcache \  
&& cd /tmp/memcache \  
&& curl -L https://github.com/php-memcached-dev/php-memcached/archive/php7.zip
-O \  
&& unzip php7.zip \  
&& cd php-memcached-php7 \  
&& phpize \  
&& ./configure \  
&& make && make install \  
&& docker-php-ext-enable imagick json memcached mysqli opcache pdo pdo_mysql \  
&& cd / \  
&& rm -rf /tmp/memcache \  
&& rm -rf /tmp/pear \  
&& apk --no-cache del ${build_pkgs} \  
&& apk --no-cache add ${runtime_pkgs}  
  
CMD ["php-fpm", "-F", "-O"]  

