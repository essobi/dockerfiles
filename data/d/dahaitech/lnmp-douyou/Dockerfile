FROM wordpress:php5.6-fpm-alpine  
  
COPY root /  
  
RUN set -ex; \  
\  
apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
libmcrypt-dev; \  
\  
pecl install redis; \  
docker-php-ext-enable redis; \  
\  
docker-php-ext-install mysql pdo_mysql bcmath mcrypt; \  
\  
apk del .build-deps;  
  
ENTRYPOINT []  
CMD ["php-fpm"]

