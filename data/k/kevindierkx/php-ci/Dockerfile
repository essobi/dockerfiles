FROM php:7.1-alpine  
MAINTAINER Kevin Dierkx <kevin@pcextreme.nl>  
  
# Install libraries  
RUN apk add --no-cache --virtual .persistent-deps \  
icu-dev \  
openssh-client \  
git \  
libxml2-dev  
  
# Install PHP extensions  
ENV MEMCACHED_DEPS zlib-dev libmemcached-dev cyrus-sasl-dev  
RUN apk add --no-cache --virtual .build-deps \  
autoconf \  
make \  
g++ \  
&& apk add --no-cache --update libmemcached-libs zlib \  
&& apk add --no-cache --virtual .memcached-deps $MEMCACHED_DEPS \  
&& pecl install memcached \  
&& echo "extension=memcached.so" > /usr/local/etc/php/conf.d/20_memcached.ini
\  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl soap pdo pdo_mysql \  
&& docker-php-ext-enable soap \  
&& apk del .build-deps .memcached-deps  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN php -i  
RUN php -m  
  
CMD ["php", "-a"]  

