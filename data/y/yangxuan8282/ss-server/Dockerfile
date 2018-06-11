FROM alpine  
  
ENV SS_VER=3.1.3  
ENV SS_URL=https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz  
  
ENV SIMPLE_OBFS_VER=0.0.5  
  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
automake \  
autoconf \  
build-base \  
curl \  
libev-dev \  
libtool \  
linux-headers \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
c-ares-dev \  
git \  
tar \  
udns-dev && \  
cd /tmp && \  
git clone --depth=1 https://github.com/shadowsocks/simple-obfs.git . && \  
git submodule update --init --recursive && \  
./autogen.sh && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
rm -rf * && \  
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
apk add --no-cache --virtual .run-deps rng-tools $runDeps && \  
apk del .build-deps && \  
rm -rf /tmp/*  
  
USER nobody  
  
ENV SS_SERVER_IP=0.0.0.0 \  
SS_SERVER_PORT=8388 \  
SS_METHOD=chacha20-ietf-poly1305 \  
SS_PASSWD= \  
SS_LOCAL_PORT=1080 \  
SS_TIMEOUT=300 \  
DNS_ADDR=8.8.8.8 \  
DNS_ADDR_2=8.8.4.4 \  
SS_ARGS=  
  
EXPOSE $SS_SERVER_PORT/tcp $SS_SERVER_PORT/udp  
  
CMD ss-server -s $SS_SERVER_IP \  
-p $SS_SERVER_PORT \  
-k ${SS_PASSWD:-$(hostname)} \  
-m $SS_METHOD \  
-t $SS_TIMEOUT \  
\--fast-open \  
-d $DNS_ADDR \  
-d $DNS_ADDR_2 \  
-u \  
$SS_ARGS  
  

