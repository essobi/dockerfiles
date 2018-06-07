FROM drush/drush:8  
ENV DRUPAL_ENVIRONMENT local  
ENV DRUPAL_TMP_DIR tmp  
ENV DRUPAL_PUBLIC_DIR sites/default/files  
ENV DRUPAL_PRIVATE_DIR sites/default/files/private  
ENV SITEROOT /app  
ENV NEW_BRANCH false  
ENV MEMCACHED_HOST memcached  
ENV PROD_PORT 22  
# Install memcached php libraries  
RUN apt-get update && apt-get install -y libmemcached-dev libmemcached11
build-essential zlib1g-dev unzip || true; \  
export PHP_EXT_DIR=/usr/src/php/ext && mkdir -p /usr/src/php/ext/memcached ||
true; \  
curl -O https://codeload.github.com/php-memcached-dev/php-memcached/zip/php7
&& unzip php7 && mv php-memcached-php7/* /usr/src/php/ext/memcached && mv php-
memcached-php7/.* /usr/src/php/ext/memcached || true; \  
rm php7 && rm -rf php-memcached-php7 && docker-php-ext-install memcached  
  
COPY config/php.ini /usr/local/etc/php/  
COPY config/docker-php-ext-memcached.ini /usr/local/etc/php/conf.d/  
RUN chown root:staff /usr/local/etc/php/php.ini
/usr/local/etc/php/conf.d/docker-php-ext-memcached.ini  
  
# Copy startup script  
COPY run.sh /run.sh  
COPY wordpress_run.sh /wordpress_run.sh  
RUN chmod 777 /run.sh /wordpress_run.sh  
  
ENTRYPOINT /run.sh  

