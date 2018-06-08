# kcp-server & shadowsocks-libev for Dockerfile  
FROM alpine:latest  
# MAINTAINER cnDocker  
  
ARG SS_VER=3.0.6  
ARG SS_URL=https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz  
  
ENV CONF_DIR="/usr/local/conf"  
  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
autoconf \  
build-base \  
curl \  
libev-dev \  
libtool \  
linux-headers \  
udns-dev \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
tar \  
udns-dev && \  
  
cd /tmp && \  
curl -sSL $SS_URL | tar xz --strip 1 && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
cd .. && \  
  
runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
  
apk add --no-cache --virtual .run-deps bash $runDeps && \  
apk del .build-deps && \  
rm -rf shadowsocks-libev /tmp/*  
  
# ADD entrypoint.sh /entrypoint.sh  
# RUN chmod +x /entrypoint.sh  
# ENTRYPOINT ["/entrypoint.sh"]  

