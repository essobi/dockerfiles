# php  
#  
# Version 1.0.0  
  
FROM alpine:3.4  
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>  
  
RUN apk add --no-cache \  
php5-mcrypt \  
php5-soap \  
php5-openssl \  
php5-gmp \  
php5-pdo_odbc \  
php5-json \  
php5-dom \  
php5-pdo \  
php5-zip \  
php5-mysql \  
php5-sqlite3 \  
php5-apcu \  
php5-pdo_pgsql \  
php5-bcmath \  
php5-gd \  
php5-xcache \  
php5-odbc \  
php5-pdo_mysql \  
php5-pdo_sqlite \  
php5-gettext \  
php5-xmlreader \  
php5-xmlrpc \  
php5-bz2 \  
php5-memcache \  
php5-mssql \  
php5-iconv \  
php5-pdo_dblib \  
php5-curl \  
php5-ctype \  
php5-fpm  
  
RUN set -ex \  
&& cd /etc/php5 \  
&& mkdir php-fpm.d \  
&& cp php-fpm.conf php-fpm.d/www.conf \  
&& { \  
echo '[global]'; \  
echo 'include=/etc/php5/php-fpm.d/*.conf'; \  
} | tee php-fpm.conf \  
&& { \  
echo '[global]'; \  
echo 'error_log = /proc/self/fd/2'; \  
echo; \  
echo '[www]'; \  
echo '; if we send this to /proc/self/fd/1, it never appears'; \  
echo 'access.log = /proc/self/fd/2'; \  
echo; \  
echo 'clear_env = no'; \  
echo; \  
echo '; Ensure worker stdout and stderr are sent to the main error log.'; \  
echo 'catch_workers_output = yes'; \  
} | tee php-fpm.d/docker.conf \  
&& { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = [::]:9000'; \  
} | tee php-fpm.d/zz-docker.conf  
  
EXPOSE 9000  
  
CMD ["php-fpm"]

