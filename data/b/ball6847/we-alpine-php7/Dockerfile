FROM alpine:edge  
MAINTAINER Porawit Poboonma <ball6847@gmail.com>  
  
ENV PHP_VERSION 7.1.9-r1  
  
RUN apk add --update --no-cache \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/community/ \  
php7==$PHP_VERSION \  
php7-zip==$PHP_VERSION \  
php7-pdo==$PHP_VERSION \  
php7-pdo_mysql==$PHP_VERSION \  
php7-pdo_sqlite==$PHP_VERSION \  
php7-gd==$PHP_VERSION \  
php7-mcrypt==$PHP_VERSION \  
php7-mbstring==$PHP_VERSION \  
php7-ctype==$PHP_VERSION \  
php7-json==$PHP_VERSION \  
php7-opcache==$PHP_VERSION \  
php7-fpm==$PHP_VERSION \  
php7-mysqli==$PHP_VERSION \  
php7-curl==$PHP_VERSION \  
php7-dom==$PHP_VERSION \  
php7-intl==$PHP_VERSION \  
php7-iconv==$PHP_VERSION \  
php7-phar==$PHP_VERSION \  
php7-zlib==$PHP_VERSION \  
php7-openssl==$PHP_VERSION \  
php7-session==$PHP_VERSION \  
php7-xml==$PHP_VERSION \  
php7-fileinfo=$PHP_VERSION \  
php7-tokenizer=$PHP_VERSION \  
php7-xmlwriter=$PHP_VERSION \  
php7-bcmath=$PHP_VERSION \  
php7-redis=3.1.2-r1 \  
&& wget -qO- https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer \  
&& wget -qO- https://raw.githubusercontent.com/Eficode/wait-for/master/wait-
for > /usr/bin/wait-for \  
&& chmod +x /usr/bin/wait-for \  
&& addgroup -g 82 -S www-data && adduser -u 82 -D -S -G www-data www-data \  
&& rm -rf /var/cache/apk/*  
  
ADD conf/ /etc/php7/  
  
ENTRYPOINT ["php-fpm7"]  

