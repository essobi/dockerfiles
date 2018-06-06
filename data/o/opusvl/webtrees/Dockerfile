FROM php:7.1-fpm  
MAINTAINER Kane Valentine - OpusVL <kane.valentine@opusvl.com>  
  
RUN set -ex; \  
\  
savedAptMark="$(apt-mark showmanual)"; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libjpeg-dev \  
libpng-dev \  
; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd opcache pdo_mysql; \  
\  
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
  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN { \  
echo 'file_uploads=On'; \  
echo 'max_execution_time=80'; \  
echo 'post_max_size=128M'; \  
echo 'upload_max_filesize=128M'; \  
echo 'memory_limit=256M'; \  
} > /usr/local/etc/php/conf.d/webtrees-recommended.ini  
  
VOLUME /var/www/html  
  
ENV WEBTREES_VERSION 1.7.9  
ENV WEBTREES_SHA1 294b4bced008b4c0ef1c3979849b93b097717b39  
  
RUN set -ex; \  
curl -o webtrees.tar.gz -fSL
"https://github.com/fisharebest/webtrees/archive/${WEBTREES_VERSION}.tar.gz";
\  
echo "$WEBTREES_SHA1 *webtrees.tar.gz" | sha1sum -c -; \  
tar -xzf webtrees.tar.gz -C /usr/src/; \  
rm webtrees.tar.gz; \  
chown -R www-data:www-data /usr/src/webtrees-${WEBTREES_VERSION}  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["php-fpm"]  

