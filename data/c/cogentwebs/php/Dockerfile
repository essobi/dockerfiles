FROM cogentwebs/base  
  
MAINTAINER Pichate Ins <cogent@cogentwebworks.com>  
  
# Set labels  
LABEL com.php.cogentwebworks.version="0.1.0-beta"  
  
  
ENV PHP_MEMORY_LIMIT=512M  
ENV UPLOAD_MAX_SIZE=2G  
ENV APC_SHM_SIZE=128M  
ENV OPCACHE_MEM_SIZE=128M  
ENV PHP_LOG_LEVEL=error  
ENV PHP_TIMEOUT=300  
  
ADD https://repos.php.earth/alpine/phpearth.rsa.pub
/etc/apk/keys/phpearth.rsa.pub  
RUN echo "https://repos.php.earth/alpine/v3.7" >> /etc/apk/repositories  
  
RUN set -x ; \  
addgroup -g 82 -S www-data ; \  
adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1  
  
RUN apk-install \  
musl \  
mariadb-client \  
openssl \  
ca-certificates \  
openssl \  
php7.2-apcu \  
# php7.2-amqp \  
php7.2-bcmath \  
php7.2-bz2 \  
php7.2-calendar \  
php7.2-composer \  
php7.2-ctype \  
php7.2-curl \  
php7.2-dba \  
php7.2-dom \  
php7.2-embed \  
php7.2-enchant \  
php7.2-exif \  
php7.2-fileinfo \  
php7.2-fpm \  
php7.2-ftp \  
php7.2-gd \  
php7.2-gettext \  
php7.2-gmp \  
php7.2-iconv \  
php7.2-imagick \  
php7.2-imap \  
php7.2-intl \  
php7.2-json \  
php7.2-ldap \  
# php7.2-mailparse \  
php7.2-mongodb \  
php7.2-mbstring \  
php7.2-mcrypt \  
php7.2-memcached \  
php7.2-mysqli \  
php7.2-mysqlnd \  
php7.2-odbc \  
php7.2-opcache \  
php7.2-openssl \  
php7.2-pcntl \  
php7.2-pdo \  
php7.2-pdo_mysql \  
php7.2-pdo_pgsql \  
php7.2-pdo_sqlite \  
php7.2-pgsql \  
php7.2-phar\  
php7.2-posix \  
php7.2-pspell \  
php7.2-recode \  
php7.2-redis \  
php7.2-session \  
php7.2-shmop \  
php7.2-simplexml \  
php7.2-snmp \  
php7.2-soap \  
php7.2-sockets \  
php7.2-sodium \  
php7.2-sqlite3 \  
php7.2-tidy \  
php7.2-tokenizer \  
php7.2-wddx \  
php7.2-xdebug \  
php7.2-xml \  
php7.2-xmlreader \  
php7.2-xmlrpc \  
php7.2-xmlwriter \  
php7.2-xml \  
php7.2-zip \  
php7.2-zlib \  
# php7.2-zmq \  
&& \  
apk-clean && \  
mkdir -p /usr/html && \  
sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php/7.2/php.ini && \  
ln -s /usr/sbin/php-fpm7.2 /sbin/php-fpm  
  
# root filesystem  
COPY rootfs /  
  
EXPOSE 9000  
# INIT  
ENTRYPOINT ["/init"]  

