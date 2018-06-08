FROM sstc/php-laravel:7.0-fpm-alpine  
  
LABEL maintainer="dev@nutspie.com"  
# redis.so  
ENV PHPREDIS_VERSION 3.1.2  
RUN curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mkdir -p /usr/src/php/ext \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install redis  
  
# mongodb.so  
RUN apk add --no-cache \  
autoconf \  
g++ \  
make \  
pcre-dev \  
openssl-dev \  
&& pecl install mongodb \  
&& docker-php-ext-enable mongodb \  
&& apk del --no-cache \  
autoconf \  
g++ \  
make \  
pcre-dev \  
openssl-dev  
  
# zip  
RUN apk add --no-cache \  
zlib \  
zlib-dev \  
&& docker-php-ext-install zip \  
&& apk del --no-cache \  
zlib-dev  

