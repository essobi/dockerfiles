FROM alpine  
MAINTAINER HyperApp <hyperappcloud@gmail.com>  
  
ARG SS_VER=3.2.0  
ARG SS_OBFS_VER=0.0.5  
  
RUN set -ex && \  
apk add --no-cache udns && \  
apk add --no-cache --virtual .build-deps \  
git \  
autoconf \  
automake \  
make \  
build-base \  
curl \  
libev-dev \  
c-ares-dev \  
libtool \  
linux-headers \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
tar \  
udns-dev && \  
  
cd /tmp/ && \  
git clone https://github.com/shadowsocks/shadowsocks-libev.git && \  
cd shadowsocks-libev && \  
git checkout v$SS_VER && \  
git submodule update --init --recursive && \  
./autogen.sh && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
cd /tmp/ && \  
git clone https://github.com/shadowsocks/simple-obfs.git shadowsocks-obfs && \  
cd shadowsocks-obfs && \  
git checkout v$SS_OBFS_VER && \  
git submodule update --init --recursive && \  
./autogen.sh && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
cd .. && \  
  
runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
apk add --no-cache --virtual .run-deps $runDeps && \  
apk del .build-deps && \  
rm -rf /tmp/*  
  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8388  
ENV PASSWORD=  
ENV METHOD chacha20  
ENV TIMEOUT 300  
ENV DNS_ADDR 8.8.8.8  
ENV DNS_ADDR_2 8.8.4.4  
ENV PLUGIN=  
ENV PLUGIN_OPTS=  
ENV CONFIG=  
  
EXPOSE $SERVER_PORT/tcp  
EXPOSE $SERVER_PORT/udp  
  
  
CMD ss-server -s :: -s $SERVER_ADDR \  
-p $SERVER_PORT \  
-k "$PASSWORD" \  
-m "$METHOD" \  
-t $TIMEOUT \  
-d "$DNS_ADDR" \  
\--fast-open \  
-u $OPTIONS  

