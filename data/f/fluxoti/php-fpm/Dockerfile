FROM php:7-fpm-alpine  
MAINTAINER Fluxoti <lucas.gois@fluxoti.com>  
  
COPY . /build  
  
ENV PHP_ERROR_REPORTING=E_ALL PHP_DISPLAY_ERRORS=On PHP_MEMORY_LIMIT=512M
PHP_TIMEZONE=UTC \  
PHP_UPLOAD_MAX_FILESIZE=100M PHP_POST_MAX_SIZE=100M NR_INSTALL_SILENT=true  
  
# Removing the standard config from the original image  
RUN rm /usr/local/etc/php-fpm.d/docker.conf && rm /usr/local/etc/php-
fpm.d/www.conf && \  
rm /usr/local/etc/php-fpm.d/zz-docker.conf && \  
  
# Copying our config  
cp /build/www.conf /usr/local/etc/php-fpm.d/www.conf && \  
cp /build/php-entrypoint.sh / && chmod +x /php-entrypoint.sh && \  
cp /build/php.ini /usr/local/etc/php && \  
  
# Instaling build dependencies  
apk add \--no-cache --virtual .build-deps zlib-dev openssl-dev $PHPIZE_DEPS &&
\  
  
# Installing PHP extensions  
apk update && apk add postgresql-dev && docker-php-ext-install pdo_pgsql &&
docker-php-ext-install pdo_mysql && \  
docker-php-ext-install mbstring json && \  
pecl install mongodb zip xdebug && docker-php-ext-enable mongodb zip xdebug &&
\  
  
# Installing composer  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php composer-setup.php && mv composer.phar /bin/composer && \  
php -r "unlink('composer-setup.php');" && \  
  
# Installing nodejs and npm  
apk add nodejs && \  
  
# Installing python and build base(need for node-sass)  
apk add python build-base && \  
  
# CleanUP  
apk del .build-deps && \  
rm -rf /build  
  
VOLUME /var/www/html  
CMD ["/php-entrypoint.sh"]

