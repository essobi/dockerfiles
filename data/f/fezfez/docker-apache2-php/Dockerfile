FROM php:7.2-fpm-alpine3.6  
# Install PDO MySQL driver  
# See https://github.com/docker-library/php/issues/62  
COPY config/php.ini /usr/local/etc/php/php.ini  
  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
  
RUN apk update --update && apk add --update --no-cache icu-dev libpng-dev  
  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install gd  
  
RUN apk --no-cache add pcre-dev ${PHPIZE_DEPS}  
# Install APCu  
RUN pecl install apcu  
RUN echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini  
  
RUN curl --insecure https://getcomposer.org/composer.phar -o /usr/bin/composer
&& chmod +x /usr/bin/composer  
  
WORKDIR /var/www/  

