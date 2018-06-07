FROM alpine:3.4  
ENV KCP_VER 20180316  
ENV KCP_URL
https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-linux-
amd64-$KCP_VER.tar.gz  
  
ENV SS_VER 3.1.3  
ENV SS_URL https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz  
  
RUN apk update && \  
apk upgrade && \  
apk add --update bash curl python openssl-dev && \  
# get kcpclient  
curl -sSL "$KCP_URL" | tar -xvzC /bin/  
  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
autoconf \  
build-base \  
curl \  
libev-dev \  
linux-headers \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
tar \  
c-ares-dev && \  
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
apk add \--no-cache --virtual .run-deps $runDeps && \  
apk del .build-deps && \  
rm -rf /tmp/*  
  
ADD init ./  
ENTRYPOINT ./init  

