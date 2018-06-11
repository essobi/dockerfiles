# From PHP 7.1 CLI image based on Alpine Linux  
FROM php:7.1-cli-alpine  
  
# Maintainer  
MAINTAINER Alexander Graf <alex@basecamp.tirol>  
  
# Configuration  
ENV HTTP_PORT 80  
\  
# Install dependencies  
RUN apk --no-cache add --virtual .build-deps $PHPIZE_DEPS \  
&& apk --no-cache add --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community --virtual .ext-deps gcc g++
pkgconfig autoconf automake make g++ libtool nasm libmcrypt-dev freetype-dev \  
libjpeg-turbo-dev libpng-dev shadow curl curl-dev libxml2-dev icu-dev msmtp
openssl-dev optipng pngquant libintl icu \  
&& apk --no-cache add --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community --repository http://dl-
cdn.alpinelinux.org/alpine/edge/main --repository http://dl-
cdn.alpinelinux.org/alpine/v3.6/community nodejs-current nodejs-current-npm \  
&& docker-php-source extract \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install soap pcntl curl dom gd hash iconv intl json mbstring
mysqli opcache pdo pdo_mysql session sockets tokenizer xml zip \  
&& yes '' | pecl install apcu-5.1.8 xdebug \  
&& docker-php-ext-enable apcu \  
&& docker-php-ext-enable xdebug \  
&& docker-php-source delete \  
&& rm -rf /var/cache/apk/*  
  
# Install composer  
RUN curl --silent --show-error https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/bin --filename=composer  
  
# Hack to change uid of 'www-data' to 1000  
RUN usermod -u 1000 www-data  
  
# Change working directory  
WORKDIR /srv  
  
# HTTP port should be exposed  
EXPOSE ${HTTP_PORT}  
  
# UTF-8 default  
ENV LANG en_US.utf8  
  
# Entrypoint is artisan  
ENTRYPOINT ["php", "artisan"]  
  
# Default command is 'serve#  
CMD ["serve", "--host=0.0.0.0", "--port=${HTTP_PORT}", "-vv"]  

