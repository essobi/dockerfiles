FROM alpine:edge  
  
ARG NEXTCLOUD_VERSION="12.0.2"  
ENV UID=1000 GID=1000 \  
UPLOAD_MAX_SIZE=10G \  
APC_SHM_SIZE=128M \  
OPCACHE_MEM_SIZE=128 \  
MEMORY_LIMIT=512M \  
CRON_PERIOD=15m \  
CRON_MEMORY_LIMIT=1g \  
TZ=Etc/UTC \  
DB_TYPE=sqlite3 \  
DOMAIN=localhost \  
EMAIL=hostmaster@localhost  
  
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& echo "http://nl.alpinelinux.org/alpine/v3.5/main" >> /etc/apk/repositories
\  
&& BUILD_DEPS=" \  
gnupg \  
tar \  
build-base \  
autoconf \  
automake \  
pcre-dev \  
libtool \  
libffi-dev \  
openssl-dev \  
python-dev \  
samba-dev" \  
&& apk -U upgrade && apk add \  
${BUILD_DEPS} \  
bash \  
nginx \  
python \  
py-pip \  
openssl \  
s6 \  
libressl \  
libressl2.4-libcrypto \  
ca-certificates \  
libsmbclient \  
samba-client \  
su-exec \  
tzdata \  
php7 \  
php7-fpm \  
php7-intl \  
php7-mbstring \  
php7-curl \  
php7-gd \  
php7-fileinfo \  
php7-mcrypt \  
php7-opcache \  
php7-json \  
php7-session \  
php7-pdo \  
php7-dom \  
php7-ctype \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pgsql \  
php7-pdo_sqlite \  
php7-sqlite3 \  
php7-zlib \  
php7-zip \  
php7-xmlreader \  
php7-xml \  
php7-xmlwriter \  
php7-posix \  
php7-openssl \  
php7-ldap \  
php7-ftp \  
php7-pcntl \  
php7-exif \  
php7-redis \  
php7-iconv \  
php7-pear \  
php7-dev \  
&& pecl install smbclient redis apcu \  
&& echo "extension=smbclient.so" > /etc/php7/conf.d/00_smbclient.ini \  
&& echo "extension=redis.so" > /etc/php7/conf.d/00_redis.ini \  
&& sed -i 's|;session.save_path = "/tmp"|session.save_path =
"/data/session"|g' /etc/php7/php.ini \  
&& pip install -U pip \  
&& pip install -U certbot \  
&& mkdir -p /etc/letsencrypt/webrootauth /etc/letsencrypt/live/localhost
/etc/letsencrypt/archive \  
&& mkdir /nextcloud \  
&& NEXTCLOUD_TARBALL="nextcloud-${NEXTCLOUD_VERSION}.tar.bz2" \  
&& wget -q https://download.nextcloud.com/server/releases/${NEXTCLOUD_TARBALL}
\  
&& tar xjf ${NEXTCLOUD_TARBALL} \--strip 1 -C /nextcloud \  
&& apk del ${BUILD_DEPS} php7-pear php7-dev \  
&& rm -rf /var/cache/apk/* /tmp/* /root/.gnupg  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm.conf /etc/php7/php-fpm.conf  
COPY opcache.ini /etc/php7/conf.d/00_opcache.ini  
COPY apcu.ini /etc/php7/conf.d/apcu.ini  
COPY run.sh /usr/local/bin/run.sh  
COPY setup.sh /usr/local/bin/setup.sh  
COPY occ /usr/local/bin/occ  
COPY s6.d /etc/s6.d  
COPY generate-certs /usr/local/bin/generate-certs  
COPY letsencrypt-setup /usr/local/bin/letsencrypt-setup  
COPY letsencrypt-renew /usr/local/bin/letsencrypt-renew  
  
RUN { \  
echo 'opcache.enable=1'; \  
echo 'opcache.enable_cli=1'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=10000'; \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.save_comments=1'; \  
echo 'opcache.revalidate_freq=1'; \  
} > /etc/php7/conf.d/00_opcache.ini  
  
RUN chmod +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
VOLUME /data /config /apps2  
  
EXPOSE 8080 8443  
LABEL description="A server software for creating file hosting services" \  
nextcloud="Nextcloud v${NEXTCLOUD_VERSION}" \  
maintainer="ull <methodreturn@gmail.com>"  
  
CMD ["run.sh"]  

