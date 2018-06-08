FROM php:fpm-alpine  
  
RUN apk add --no-cache \  
libmcrypt-dev \  
openldap-dev && \  
apk add --no-cache --virtual .phpize-deps \  
${PHPIZE_DEPS} && \  
docker-php-ext-install mcrypt && \  
docker-php-ext-install ldap && \  
docker-php-ext-install pdo_mysql && \  
pecl install redis-3.1.2 && \  
docker-php-ext-enable redis && \  
docker-php-source delete && \  
apk del .phpize-deps  
  

