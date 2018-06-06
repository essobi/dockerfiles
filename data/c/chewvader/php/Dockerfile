# https://github.com/docker-
library/wordpress/blob/1caade96b306d0ed12f5637196e8f0b1883330f5/php7.1/fpm/Dockerfile  
FROM php:7.1.16-fpm  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
savedAptMark="$(apt-mark showmanual)"; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libjpeg-dev \  
libpng-dev \  
libzip-dev \  
; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache zip; \  
\  
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all
build dependencies  
apt-mark auto '.*' > /dev/null; \  
apt-mark manual $savedAptMark; \  
ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \  
| awk '/=>/ { print $3 }' \  
| sort -u \  
| xargs -r dpkg-query -S \  
| cut -d: -f1 \  
| sort -u \  
| xargs -rt apt-mark manual; \  
\  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false;
\  
rm -rf /var/lib/apt/lists/*  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  

