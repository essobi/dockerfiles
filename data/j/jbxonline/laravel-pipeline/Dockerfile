FROM php:7.2-fpm-alpine  
  
RUN apk update && apk add curl && \  
curl -sS https://getcomposer.org/installer | php \  
&& chmod +x composer.phar && mv composer.phar /usr/local/bin/composer  
  
RUN apk \--no-cache add --virtual .build-deps $PHPIZE_DEPS \  
&& apk \--no-cache add --virtual .ext-deps libmcrypt-dev freetype-dev git \  
libjpeg-turbo-dev libpng-dev libxml2-dev msmtp bash openssl-dev pkgconfig \  
icu-dev nodejs openssh yarn \  
&& docker-php-source extract \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd mysqli pdo pdo_mysql zip opcache intl soap \  
&& pecl install redis xdebug \  
&& docker-php-ext-enable xdebug \  
&& docker-php-source delete \  
&& apk del .build-deps  
  
WORKDIR /var/www/html  
  
LABEL maintainer="Jon Bowes <jon@jbxonline.net>"  

