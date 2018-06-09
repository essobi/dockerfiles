FROM php:7.1.7-fpm-alpine  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apk upgrade --update && \  
apk add \  
autoconf \  
make \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
zlib-dev \  
icu-dev \  
g++ \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
docker-php-ext-configure intl; \  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install intl gd mysqli opcache mbstring  
  
ADD config.ini /usr/local/etc/php/conf.d/config.ini  
  
RUN yes | pecl install xdebug && \  
echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" >
/usr/local/etc/php/conf.d/xdebug-enable.ini;  
  
VOLUME ["/var/www/html"]  
  
EXPOSE 9000  
  
CMD ["php-fpm"]

