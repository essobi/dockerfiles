from zacksleo/docker-composer:alpine  
RUN apk add libmemcached-dev cyrus-sasl-dev  
RUN pecl install memcached-3.0.4 && docker-php-ext-enable memcached

