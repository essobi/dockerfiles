FROM alpine:latest  
  
LABEL description "Adminer is a full-featured database management tool"  
# this fork is maintained by kleberbaum  
MAINTAINER Florian Kleber <kleberbaum@erebos.xyz>  
  
ARG VERSION=4.3.1  
ARG
SHA256_HASH="c26f48bc06c195928dee9ca5d5a485d86a8b14d420368061fd8045ac26fcc701"  
  
ENV GID=991 UID=991  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories && \  
echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories && \  
apk upgrade --update-cache --available && \  
apk add --no-cache --virtual=build-dependencies \  
ca-certificates \  
openssl && \  
apk add --force \  
su-exec \  
tini@community \  
php7@community \  
php7-session@community \  
php7-pdo_mysql@community \  
php7-pdo_pgsql@community \  
php7-pdo_sqlite@community && \  
cd /tmp \  
\  
# Download and install adminer and pepa-linha theme  
&& ADMINER_FILE="adminer-${VERSION}.php" \  
&& wget -q
https://github.com/vrana/adminer/releases/download/v${VERSION}/${ADMINER_FILE}
\  
&& echo "Verifying integrity of ${ADMINER_FILE}..." \  
&& CHECKSUM=$(sha256sum ${ADMINER_FILE} | awk '{print $1}') \  
&& if [ "${CHECKSUM}" != "${SHA256_HASH}" ]; then echo "ERROR: Checksum does
not match!" && exit 1; fi \  
&& echo "All seems good, hash is valid." \  
&& mkdir /adminer && mv ${ADMINER_FILE} /adminer/index.php \  
&& wget -q
https://raw.githubusercontent.com/vrana/adminer/master/designs/pepa-
linha/adminer.css -P /adminer \  
&& apk del build-dependencies \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*  
  
EXPOSE 8888  
# place init  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
# I personally like to start my containers with tini  
ENTRYPOINT ["/sbin/tini", "--", "/run.sh"]  

