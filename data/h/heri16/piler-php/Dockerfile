FROM php:fpm-alpine  
  
RUN apk add \--no-cache freetype libpng libjpeg-turbo libmemcached-libs
c-client freetype-dev libpng-dev libjpeg-turbo-dev libmemcached-dev cyrus-
sasl-dev imap-dev openssl-dev && \  
mkdir -p /usr/src/php/ext/memcached && \  
curl -L https://github.com/php-memcached-dev/php-memcached/archive/php7.tar.gz
| tar \--strip-components=1 -xzC /usr/src/php/ext/memcached && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
docker-php-ext-configure memcached \--disable-memcached-sasl && \  
docker-php-ext-configure imap \--with-imap-ssl && \  
NPROC=$(getconf _NPROCESSORS_ONLN) && \  
docker-php-ext-install -j${NPROC} pdo pdo_mysql mbstring gd memcached imap &&
\  
apk del \--no-cache freetype-dev libpng-dev libjpeg-turbo-dev libmemcached-dev
cyrus-sasl-dev imap-dev openssl-dev  
  
RUN apk add \--no-cache mariadb-client-libs libintl git gettext-dev openssl-
dev mariadb-dev build-base automake autoconf libtool && \  
NPROC=$(getconf _NPROCESSORS_ONLN) && \  
mkdir -p /usr/src/tre && \  
curl -L https://github.com/laurikari/tre/archive/master.tar.gz | tar \--strip-
components=1 -xzC /usr/src/tre && \  
cd /usr/src/tre && ./utils/autogen.sh && ./configure \--prefix=/usr && make
-j${NPROC} && make install && \  
addgroup -g 1001 piler && adduser -u 1001 -G piler -s /bin/sh -h /var/piler -D
piler && passwd -dl piler || true && \  
mkdir -p /usr/src/piler && \  
curl -L https://bitbucket.org/jsuto/piler/downloads/piler-1.2.0.tar.gz | tar
\--strip-components=1 -xzC /usr/src/piler && \  
cd /usr/src/piler && ./configure \--localstatedir=/var \--with-database=mysql
\--disable-starttls && make -j${NPROC} && make install && \  
chmod 6755 /usr/local/bin/piler* /usr/local/bin/reindex && \  
sed -e'/load_default_values$/q' ./util/postinstall.sh > /tmp/postinstall.sh &&
\  
cd /tmp && echo $'make_cron_entries\ncrontab -u $PILERUSER
$CRON_TMP\nclean_up_temp_stuff' >> postinstall.sh && sh postinstall.sh && rm
postinstall.sh && \  
ln -s /usr/local/bin/php /usr/bin/php && \  
apk del \--no-cache git gettext-dev openssl-dev mariadb-dev build-base
automake autoconf libtool  
  
#EXPOSE 9000/tcp  
  
ADD run.sh /sbin/run.sh  
  
CMD ["/sbin/run.sh"]  

