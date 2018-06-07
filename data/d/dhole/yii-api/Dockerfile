FROM richarvey/nginx-php-fpm:latest  
MAINTAINER Barry "dhole.me@gmail.com"  
RUN docker-php-ext-configure bcmath \  
&& docker-php-ext-configure pcntl \  
&& docker-php-ext-configure sockets \  
&& docker-php-ext-install bcmath pcntl sockets  
  
ENV MEMCACHED_DEPS zlib-dev libmemcached-dev cyrus-sasl-dev  
RUN apk add --update libmemcached-libs zlib  
RUN apk add --update --virtual .phpize-deps $PHPIZE_DEPS \  
&& apk add --update --virtual .memcached-deps $MEMCACHED_DEPS \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached  
  
RUN pecl install mongodb \  
# && pecl install redis \  
&& pecl install xdebug \  
&& docker-php-ext-enable mongodb  
  
RUN sed -i '5d' /etc/nginx/sites-enabled/default.conf \  
&& sed -i '5i root /var/www/html/api/web;' /etc/nginx/sites-
enabled/default.conf \  
&& sed -i '24i if (!-e $request_filename){ rewrite ^/(.*) /index.php?r=$1
last; } ' /etc/nginx/sites-enabled/default.conf  

