FROM php:7-fpm-alpine  
  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories && \  
apk update && \  
apk add recode gnumeric font-adobe-100dpi git freetype libpng libjpeg-turbo
icu-libs postgresql-libs && \  
apk add --virtual .build-deps shadow autoconf gcc make g++ zlib-dev file g++
libc-dev make pkgconf freetype-dev libpng-dev libjpeg-turbo-dev icu-dev
postgresql-dev && \  
docker-php-ext-install gd intl pdo_pgsql zip exif && \  
pecl install xdebug-2.5.0 && \  
docker-php-ext-enable xdebug && \  
usermod -u 1000 www-data && \  
chown www-data /var/www && \  
mkdir -p /var/www && \  
apk del .build-deps && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer && \  
composer global require "hirak/prestissimo:^0.3" && \  
composer clear-cache  
  
RUN set -ex && \  
cd /usr/local/etc && \  
{ \  
echo 'memory_limit = -1'; \  
echo 'max_execution_time = -1'; \  
echo 'max_input_vars = 1000000'; \  
echo 'max_file_uploads = 1000000'; \  
echo 'post_max_size = 4096M'; \  
echo 'upload_max_filesize = 4096M'; \  
echo ; \  
echo 'xdebug.remote_enable = 1'; \  
echo 'xdebug.remote_connect_back = 1'; \  
echo 'xdebug.idekey = PHPSTORM'; \  
echo 'xdebug.remote_port = 9000'; \  
} | tee php/php.ini  
  
WORKDIR /var/www  

