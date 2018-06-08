FROM wonderfall/nginx-php:7.1  
  
ARG NEXTCLOUD_VERSION=12.0.0  
ARG GPG_nextcloud="2880 6A87 8AE4 23A2 8372 792E D758 99B9 A724 937A"  
  
LABEL org.freenas.interactive="false" \  
org.freenas.version="12.0.0" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.port-mappings="8888:8888/tcp" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="8888" \  
org.freenas.web-ui-path="" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/data\", \  
\"descr\": \"Nextcloud Data\" \  
}, \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Nextcloud config.php location\" \  
}, \  
{ \  
\"name\": \"/apps2\", \  
\"descr\": \"Nextcloud Downloaded Apps\" \  
}, \  
{ \  
\"name\": \"/nextcloud/themes\", \  
\"descr\": \"Nextcloud Themes Location\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"UID\", \  
\"descr\": \"User ID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"GID\", \  
\"descr\": \"Group ID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"UPLOAD_MAX_SIZE\", \  
\"descr\": \"maximum upload size (default : 10G)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"APC_SHM_SIZE\", \  
\"descr\": \"apc memory size (default : 128M)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPCACHE_MEM_SIZE\", \  
\"descr\": \"opcache memory size in megabytes (default : 128)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MEMORY_LIMIT\", \  
\"descr\": \"php memory limit (default : 512M)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CRON_PERIOD\", \  
\"descr\": \"time interval between two cron tasks (default : 15m)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CRON_MEMORY_LIMIT\", \  
\"descr\": \"memory limit for PHP when executing cronjobs (default : 1024m)\",
\  
\"optional\": true \  
}, \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"the system/log timezone (default : Etc/UTC)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ADMIN_USER\", \  
\"descr\": \"username of the admin account (default : none, web
configuration)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ADMIN_PASSWORD\", \  
\"descr\": \"password of the admin account (default : none, web
configuration)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DOMAIN\", \  
\"descr\": \"domain to use during the setup (default : localhost)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_TYPE\", \  
\"descr\": \"database type (sqlite3, mysql or pgsql) (default : sqlite3)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_NAME\", \  
\"descr\": \"name of database (default : none)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_USER\", \  
\"descr\": \"username for database (default : none)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_PASSWORD\", \  
\"descr\": \"password for database user (default : none)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_HOST\", \  
\"descr\": \"database host (default : none)\", \  
\"optional\": true \  
} \  
]"  
  
ENV UID=991 GID=991 \  
UPLOAD_MAX_SIZE=10G \  
APC_SHM_SIZE=128M \  
OPCACHE_MEM_SIZE=128 \  
MEMORY_LIMIT=512M \  
CRON_PERIOD=15m \  
CRON_MEMORY_LIMIT=1g \  
TZ=America/Edmonton \  
DB_TYPE=mysql \  
DOMAIN=localhost  
  
RUN BUILD_DEPS=" \  
gnupg \  
tar \  
build-base \  
autoconf \  
automake \  
pcre-dev \  
libtool \  
samba-dev" \  
&& apk -U upgrade && apk add \  
${BUILD_DEPS} \  
libressl \  
ca-certificates \  
libsmbclient \  
tzdata \  
tesseract-ocr \  
&& pecl install smbclient apcu redis \  
&& echo "extension=smbclient.so" > /php/conf.d/smbclient.ini \  
&& echo "extension=redis.so" > /php/conf.d/redis.ini \  
&& mkdir /nextcloud \  
&& cd /tmp \  
&& NEXTCLOUD_TARBALL="nextcloud-${NEXTCLOUD_VERSION}.tar.bz2" \  
&& wget -q https://download.nextcloud.com/server/releases/${NEXTCLOUD_TARBALL}
\  
&& wget -q
https://download.nextcloud.com/server/releases/${NEXTCLOUD_TARBALL}.sha512 \  
&& wget -q
https://download.nextcloud.com/server/releases/${NEXTCLOUD_TARBALL}.asc \  
&& wget -q https://nextcloud.com/nextcloud.asc \  
&& echo "Verifying both integrity and authenticity of ${NEXTCLOUD_TARBALL}..."
\  
&& CHECKSUM_STATE=$(echo -n $(sha512sum -c ${NEXTCLOUD_TARBALL}.sha512) | tail
-c 2) \  
&& if [ "${CHECKSUM_STATE}" != "OK" ]; then echo "Warning! Checksum does not
match!" && exit 1; fi \  
&& gpg --import nextcloud.asc \  
&& FINGERPRINT="$(LANG=C gpg --verify ${NEXTCLOUD_TARBALL}.asc
${NEXTCLOUD_TARBALL} 2>&1 \  
| sed -n "s#Primary key fingerprint: \(.*\)#\1#p")" \  
&& if [ -z "${FINGERPRINT}" ]; then echo "Warning! Invalid GPG signature!" &&
exit 1; fi \  
&& if [ "${FINGERPRINT}" != "${GPG_nextcloud}" ]; then echo "Warning! Wrong
GPG fingerprint!" && exit 1; fi \  
&& echo "All seems good, now unpacking ${NEXTCLOUD_TARBALL}..." \  
&& tar xjf ${NEXTCLOUD_TARBALL} --strip 1 -C /nextcloud \  
&& update-ca-certificates \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/* /tmp/* /root/.gnupg  
  
COPY rootfs /  
  
RUN chmod +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
VOLUME /data /config /apps2 /nextcloud/themes  
  
EXPOSE 8888  
  
LABEL description="A server software for creating file hosting services" \  
nextcloud="Nextcloud v${NEXTCLOUD_VERSION}" \  
maintainer="Wonderfall <wonderfall@targaryen.house>"  
  
CMD ["run.sh"]  

