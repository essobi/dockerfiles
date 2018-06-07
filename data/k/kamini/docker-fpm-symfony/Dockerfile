FROM php:7-fpm-alpine  
  
RUN apk add --no-cache --virtual .persistent-deps \  
acl \  
icu-libs \  
libpq \  
freetype \  
libjpeg-turbo \  
libpng \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
icu-dev \  
postgresql-dev \  
zlib-dev \  
&& docker-php-ext-install \  
gd \  
intl \  
opcache \  
pdo_pgsql \  
pdo_mysql \  
sockets \  
zip \  
&& apk del .build-deps  
  
ADD symfony.ini /usr/local/etc/php/conf.d/  
  
ENV HTTPD_USER www-data  
ENV CONSOLE_USER 1000  
  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["php-fpm"]  

