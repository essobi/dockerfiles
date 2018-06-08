FROM alpine:edge  
MAINTAINER Alain Knaebel <alain.knaebel@aknaebel.fr>  
  
ENV NEXTCLOUD_VERSION=11.0.8  
ENV UPLOAD_MAX_SIZE=10G  
ENV APC_SHM_SIZE=128M  
ENV OPCACHE_MEM_SIZE=128  
ENV DB_TYPE=sqlite3  
ENV ADMIN_USER=admin  
ENV ADMIN_PASSWORD=password  
  
  
RUN echo "http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
\  
&& echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& echo "http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& BUILD_DEPS="gnupg build-base autoconf automake libtool samba-dev pcre-dev"
\  
  
&& apk upgrade --update\  
&& apk add ca-certificates openssl \  
php7-fpm php7 php7-ctype php7-dom php7-gd php7-iconv php7-json php7-xml
php7-mbstring php7-posix php7-zip php7-zlib php7-xmlwriter php7-simplexml \  
php7-bcmath php7-calendar php7-dba php7-gettext php7-phar php7-shmop php7-soap
php7-sockets php7-sysvmsg php7-sysvshm php7-sysvshm php7-wddx php7-xmlreader \  
php7-sqlite3 php7-pdo_sqlite php7-pdo_mysql php7-pgsql \  
php7-curl php7-bz2 php7-intl php7-mcrypt php7-openssl \  
php7-ldap php7-ftp php7-imap \  
php7-exif php7-gmp \  
php7-memcached php7-redis \  
ffmpeg php7-pcntl php7-fileinfo \  
wget unzip libsmbclient samba-client supervisor su-exec \  
php7-opcache php7-pear php7-dev tar ${BUILD_DEPS} \  
&& sed -i "$ s|\\-n||g" /usr/bin/pecl && pecl install smbclient apcu \  
&& echo "extension=smbclient.so" > /etc/php7/conf.d/00_smbclient.ini \  
  
&& echo "date.timezone = 'UTC'" >> /etc/php7/php.ini \  
&& echo "short_open_tag = 0" >> /etc/php7/php.ini \  
  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data \  
&& echo "*/15 * * * * php7 -f /nextcloud/cron.php" > /etc/crontabs/www-data \  
&& chmod 600 /etc/crontabs/www-data \  
  
&& mkdir /nextcloud /apps2 /config /data \  
&& NEXTCLOUD_TARBALL="nextcloud-${NEXTCLOUD_VERSION}.tar.bz2" \  
&& cd /tmp && wget -q
https://download.nextcloud.com/server/releases/${NEXTCLOUD_TARBALL} \  
&& tar xjf ${NEXTCLOUD_TARBALL} --strip 1 -C /nextcloud \  
&& chown -R www-data:www-data /nextcloud \  
&& apk del ${BUILD_DEPS} php7-pear php7-dev \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
COPY ./php-fpm.conf /etc/php7/php-fpm.conf  
COPY ./opcache.ini /etc/php7/conf.d/00_opcache.ini  
COPY ./apcu.ini /etc/php7/conf.d/apcu.ini  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
COPY ./supervisord.conf /etc/supervisor/supervisord.conf  
COPY ./occ /usr/local/bin/occ  
  
VOLUME /nextcloud  
VOLUME /data  
VOLUME /config  
VOLUME /apps2  
  
EXPOSE 9000  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

