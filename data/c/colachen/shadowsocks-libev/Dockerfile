FROM alpine:3.5  
MAINTAINER cola <colachg@gmail.com>  
  
ARG SS_VER=3.1.0  
ARG SS_URL=https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz  
  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
autoconf \  
c-ares-dev \  
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
apk add \--no-cache --virtual .run-deps $runDeps && \  
apk del .build-deps && \  
rm -rf /tmp/*  
  
USER nobody  
  
EXPOSE 8388/tcp 8388/udp  
  
WORKDIR /shadowsocks  
  
ENTRYPOINT ["/usr/bin/ss-server"]  
  
CMD ["-c", "shadowsocks.json"]  

