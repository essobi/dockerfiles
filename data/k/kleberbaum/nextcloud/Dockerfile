FROM kleberbaum/nginx-php:latest  
  
LABEL description="A server software for creating file hosting services"  
# this fork is maintained by kleberbaum  
MAINTAINER Florian Kleber <kleberbaum@erebos.xyz>  
  
ENV UID=991 GID=991 \  
UPLOAD_MAX_SIZE=10G \  
APC_SHM_SIZE=128M \  
OPCACHE_MEM_SIZE=128 \  
MEMORY_LIMIT=512M \  
CRON_PERIOD=15m \  
CRON_MEMORY_LIMIT=1g \  
TZ=Etc/UTC \  
DB_TYPE=sqlite3 \  
DOMAIN=localhost  
  
RUN echo "## Installing base ##" && \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories && \  
echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories && \  
apk upgrade --update-cache --available && \  
\  
apk add --no-cache --virtual=build-dependencies \  
gnupg \  
tar \  
build-base \  
autoconf \  
automake \  
pcre-dev \  
libtool \  
samba-dev && \  
apk add --force \  
tini@community \  
dcron \  
libressl \  
ca-certificates \  
libsmbclient \  
tzdata && \  
\  
pecl install \  
smbclient \  
apcu \  
redis \  
\  
&& echo "extension=smbclient.so" > /php/conf.d/smbclient.ini \  
&& echo "extension=redis.so" > /php/conf.d/redis.ini \  
&& mkdir /nextcloud \  
&& cd /tmp \  
&& wget -q https://download.nextcloud.com/server/daily/latest.tar.bz2 \  
&& echo "Verifying checksum of latest.tar.bz2..." \  
&& wget -q https://download.nextcloud.com/server/daily/latest.tar.bz2.sha512 \  
&& echo "$(cat latest.tar.bz2.sha512 | awk '{print $1;}') latest.tar.bz2" >
latest.tar.bz2.sha512 \  
&& CHECKSUM_STATE=$(echo -n $(sha512sum -c latest.tar.bz2.sha512) | tail -c 2)
\  
&& if [ "${CHECKSUM_STATE}" != "OK" ]; then echo "Warning! Checksum does not
match!" && exit 1; fi \  
&& tar xjf latest.tar.bz2 --strip 1 -C /nextcloud \  
&& update-ca-certificates \  
&& apk del build-dependencies \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*  
  
COPY rootfs /  
  
RUN chmod +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
VOLUME /data /config /apps2 /nextcloud/themes /php/session  
  
EXPOSE 8888  
  
# place init script  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
# I personally like to start my containers with tini  
ENTRYPOINT ["/sbin/tini", "--", "/run.sh"]  

