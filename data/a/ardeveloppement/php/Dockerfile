FROM ardeveloppement/php:7.2  
# https://medium.com/@pablofmorales/xdebug-with-docker-and-
phpstorm-786da0d0fad2  
ENV XDEBUGINI_PATH=/usr/local/etc/php/conf.d/xdebug.ini  
ENV XDEBUG_VERSION=2.6.0  
# persistent / runtime deps  
ENV PHPIZE_DEPS \  
autoconf \  
cmake \  
file \  
g++ \  
gcc \  
libc-dev \  
pcre-dev \  
make \  
pkgconf \  
re2c  
  
# Install Requirements  
RUN set -xe \  
&& apk update \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS  
  
RUN yes | pecl install xdebug-$XDEBUG_VERSION \  
&& docker-php-ext-enable xdebug \  
&& echo "zend_extension="`find /usr/local/lib/php/extensions/ -iname
'xdebug.so'` > $XDEBUGINI_PATH  
  
# clean packages and sources  
RUN apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
COPY conf/php.dev.ini /usr/local/etc/php/php.ini  
COPY conf/xdebug.ini /tmp/xdebug.ini  
  
RUN cat /tmp/xdebug.ini >> $XDEBUGINI_PATH  
#RUN echo "xdebug.remote_host="`/sbin/ip route|awk '/default/ { print $3 }'`
>> $XDEBUGINI_PATH

