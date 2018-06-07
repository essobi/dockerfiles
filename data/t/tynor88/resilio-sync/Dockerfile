FROM quay.io/justcontainers/base-alpine:v0.12.2  
MAINTAINER tynor88 <tynor@hotmail.com>  
  
# s6 environment settings  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
ENV S6_KEEP_ENV=1  
# resilio-sync enviroment settings  
ENV GLIBC_VERSION="2.23-r3"  
ENV RESILIO_SYNC_VERSION="2.4.1"  
# install build packages  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
ca-certificates \  
wget && \  
  
update-ca-certificates && \  
  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget -P /tmp/ https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
apk add /tmp/glibc-${GLIBC_VERSION}.apk && \  
  
wget -q -P /tmp/ https://download-
cdn.getsync.com/${RESILIO_SYNC_VERSION}/linux-x64/resilio-sync_x64.tar.gz && \  
mkdir -p /app/resilio-sync && \  
tar -xzvf /tmp/resilio-sync_x64.tar.gz -C /app/resilio-sync && \  
  
apk add \--no-cache --repository
http://nl.alpinelinux.org/alpine/edge/community \  
shadow && \  
  
# cleanup  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/tmp/* \  
/var/tmp/* \  
/var/cache/apk/* \  
/etc/apk/keys/sgerrand.rsa.pub  
  
# create abc user  
RUN \  
groupmod -g 1000 users && \  
useradd -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
  
# create some files / folders  
mkdir -p /config /app /defaults  
  
# add local files  
COPY root/ /  
  
ENTRYPOINT ["/init"]  
  
EXPOSE 8888 55555  
VOLUME ["/config"]

