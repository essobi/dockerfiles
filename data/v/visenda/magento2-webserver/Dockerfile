FROM visenda/php-webserver:latest  
  
MAINTAINER Adis Heric <adis.heric@visenda.com>  
  
# additional env vars  
ENV \  
# MAGENTO  
MAGENTO_CRYPT_KEY="dc5859cfafff764fe7586a7de4d180f4" \  
MAGENTO_BASE_URL="http://192.168.99.100/" \  
MAGENTO_BACKEND_FRONTNAME="admin" \  
MAGENTO_ADMIN_FIRSTNAME="VISENDA" \  
MAGENTO_ADMIN_LASTNAME="IT" \  
MAGENTO_ADMIN_EMAIL="it@visenda.com" \  
MAGENTO_ADMIN_USER="admin" \  
MAGENTO_ADMIN_PASS="admin" \  
MAGENTO_LANGUAGE="de_DE" \  
MAGENTO_CURRENCY="EUR" \  
MAGENTO_USE_REWRITES="0" \  
MAGENTO_USE_SECURE="0" \  
\  
# REDIS  
REDIS_HOSTNAME="redis" \  
REDIS_PORT="6379" \  
REDIS_PASSWORD="" \  
\  
PHP_MEMORY_LIMIT="512M" \  
PHP_MAX_EXEC_TIME="18000" \  
PHP_UPLOAD_MAX_FILESIZE="256M" \  
PHP_POST_MAX_SIZE="256M"  
# non-persistent build deps  
RUN apk add --no-cache --virtual .build-deps \  
autoconf \  
gcc \  
libc-dev \  
make  
  
# add php extensions  
RUN echo no | pecl install \  
redis \  
&& docker-php-ext-enable \  
redis \  
# clean up  
&& docker-php-source delete \  
&& apk del .build-deps  
  
# install resources  
COPY resources/scripts/ $SCRIPTS_DIR  
RUN chmod +x $SCRIPTS_DIR/*  
  
# install source files  
COPY src/ $NGINX_WEBROOT  
RUN chown -R 1000:1001 $NGINX_WEBROOT \  
&& chmod -R 775 $NGINX_WEBROOT  
  
CMD ["/entrypoint.sh"]  

