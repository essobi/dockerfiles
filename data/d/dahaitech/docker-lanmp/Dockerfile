FROM php:7.2-fpm-alpine  
  
COPY root /  
  
ENV PHPIZE_DEPS \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c  
  
RUN apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS  
  
RUN docker-php-ext-enable opcache  
  
RUN apk add --no-cache libmcrypt-dev openssl libpng-dev libjpeg-turbo-dev
freetype-dev libssh2-dev git\  
&& docker-php-ext-configure gd --with-png-dir --with-jpeg-dir --with-freetype-
dir\  
&& docker-php-ext-install gd  
  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install pdo_mysql  
  
RUN pecl install ssh2-1.1.2 && docker-php-ext-enable ssh2  
  
RUN apk del .build-deps  
  
RUN { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = /tmp/php-fpm.socket'; \  
echo 'listen.owner = root'; \  
echo 'listen.group = root'; \  
echo 'listen.mode = 777'; \  
} | tee /usr/local/etc/php-fpm.d/zz-docker.conf  
  
RUN apk add --no-cache supervisor \  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx  
  
WORKDIR /usr/share/nginx/html  
  
CMD ["/bin/run.sh"]  

