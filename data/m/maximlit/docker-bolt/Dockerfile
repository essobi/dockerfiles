FROM alpine:latest  
  
MAINTAINER Olivier Pichon <op@united-asian.com>  
  
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk update && apk add --update \  
curl \  
git \  
nginx \  
php-cli \  
php-ctype \  
php-curl \  
php-dom \  
php-fpm \  
php-gd \  
php-json \  
php-mcrypt \  
php-openssl \  
php-pdo_mysql \  
php-pdo_sqlite \  
php-phar \  
php-xml \  
php-zip \  
php-zlib \  
shadow \  
supervisor \  
&& adduser -D -S -h /var/www -s /sbin/nologin -G www-data www-data \  
&& usermod -u 1000 www-data \  
&& rm -rf /var/www \  
&& cd /var \  
&& git clone git://github.com/bolt/bolt.git www \  
&& cd www \  
&& git checkout v3.0.1 \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer install  
  
COPY supervisord.conf /etc/supervisord.conf  
  
COPY supervisor.d/nginx.ini /etc/supervisor.d/nginx.ini  
  
COPY entrypoint.sh /entrypoint.sh  
  
COPY entrypoint.d /entrypoint.d  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
  
COPY nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf  
  
COPY supervisor.d/php-fpm.ini /etc/supervisor.d/php-fpm.ini  
  
COPY php/php-fpm.conf /etc/php/php-fpm.conf  
  
COPY php/pool.d /etc/php/pool.d  
  
VOLUME /var/www  
  
WORKDIR /var/www  
  
EXPOSE 80 443  
ENTRYPOINT "/entrypoint.sh"  

