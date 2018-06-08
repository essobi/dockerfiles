FROM alpine  
  
#WORKDIR /var/www/html  
  
ENV NEXTCLOUD_VERSION 13.0.2  
ENV NEXTCLOUD_DATA_DIR "/var/www/data"  
  
RUN set -xe \  
&& apk update \  
&& apk add --no-cache ca-certificates \  
gzip \  
nginx \  
openssl \  
php7 \  
php7-fpm \  
php7-redis \  
php7-openssl \  
php7-pdo_sqlite \  
php7-sqlite3 \  
php7-pdo_mysql \  
php7-xml \  
php7-zlib \  
php7-gd \  
php7-apcu \  
php7-xmlreader \  
php7-xmlwriter \  
php7-mbstring \  
php7-ctype \  
php7-curl \  
php7-zip \  
php7-simplexml \  
php7-iconv \  
php7-json \  
php7-dom \  
php7-posix \  
php7-opcache \  
php7-fileinfo \  
curl \  
rsync \  
tar \  
&& touch /etc/php7/php-fpm.d/empty.conf  
  
RUN set -ex; \  
curl -fsSL -o nextcloud.tar.bz2 \  
"https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2";
\  
tar -xjf nextcloud.tar.bz2 -C /root/; \  
rm nextcloud.tar.bz2; \  
rm -rf /root/nextcloud/updater; \  
mkdir -p /root/nextcloud/data; \  
mkdir -p /root/nextcloud/custom_apps; \  
mkdir -p /var/www/data; \  
mkdir -p /var/www/html/config; \  
chmod +x /root/nextcloud/occ; \  
sed -ie "s/^user =.*/user = nobody/g" /etc/php7/php-fpm.conf; \  
sed -ie "s/^group =.*/group = nobody/g" /etc/php7/php-fpm.conf; \  
sed -ie "s/^;syslog.facility =.*/syslog.facility = daemon/g" /etc/php7/php-
fpm.conf; \  
sed -ie "s/^;syslog.ident = .*/syslog.ident = php-fpm/g" /etc/php7/php-
fpm.conf; \  
sed -ie "s/^pm.max_children = .*/pm.max_children = 50/g" /etc/php7/php-
fpm.conf; \  
sed -ie "s/^;open_basedir =
.*/open_basedir=\/var\/www\/:\/tmp\/:\/data\/:\/dev\/urandom:\/proc\/meminfo/g"
/etc/php7/php.ini  
  
COPY *.sh /  
COPY config/* /root/nextcloud/config/  
COPY apps.tgz /root/nextcloud/custom_apps/  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN cd /root/nextcloud/custom_apps/ && tar -xvf apps.tgz  
  
VOLUME [$NEXTCLOUD_DATA_DIR]  
  
RUN chmod 755 $NEXTCLOUD_DATA_DIR && \  
chmod 755 /var/www/html/config && \  
chown nobody: $NEXTCLOUD_DATA_DIR && \  
chown nobody: /var/www/html/config  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm7 && nginx"]  
#CMD /bin/sh  

