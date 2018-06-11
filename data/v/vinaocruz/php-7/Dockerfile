FROM php:7.2-fpm-alpine3.7  
RUN apk add --no-cache \  
\--virtual .phpize_deps \  
$PHPIZE_DEPS \  
libxml2-dev \  
libressl-dev  
  
RUN pecl install mongodb \  
&& docker-php-ext-enable mongodb \  
&& docker-php-ext-install pdo_mysql zip soap  
  
RUN apk del .phpize_deps  
  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/local/bin --filename=composer

