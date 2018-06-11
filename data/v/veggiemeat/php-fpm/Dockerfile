FROM php:5.6-fpm-alpine  
  
RUN set -ex; \  
apk add \--no-cache --virtual .build-deps \  
libjpeg-turbo-dev \  
libpng-dev \  
&& docker-php-ext-configure gd \--with-png-dir=/usr \--with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring mysqli opcache pdo pdo_mysql zip  
  
CMD ["php-fpm"]  

