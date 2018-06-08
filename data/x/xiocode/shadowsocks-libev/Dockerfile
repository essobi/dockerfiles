#  
# Dockerfile for shadowsocks-libev  
#  
  
FROM alpine:edge  
MAINTAINER Tony.Shao <xiocode@gmail.com>  
  
ARG SS_VER=3.1.2  
ARG SS_OBFS_VER=0.0.5  
  
ARG SS_URL=https://github.com/shadowsocks/shadowsocks-
libev/archive/v$SS_VER.tar.gz  
ARG SS_OBFS_URL=https://github.com/shadowsocks/simple-
obfs/archive/v$SS_OBFS_VER.tar.gz  
  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
git \  
autoconf \  
automake \  
make \  
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
c-ares-dev && \  
  
cd /tmp/ && \  
git clone https://github.com/shadowsocks/shadowsocks-libev.git && \  
cd shadowsocks-libev && \  
git checkout v$SS_VER && \  
git submodule update --init --recursive && \  
./autogen.sh && \  
./configure \--prefix=/usr --disable-documentation && \  
make install && \  
cd /tmp/ && \  
git clone https://github.com/shadowsocks/simple-obfs.git shadowsocks-obfs && \  
cd shadowsocks-obfs && \  
git checkout v$SS_OBFS_VER && \  
git submodule update --init --recursive && \  
./autogen.sh && \  
./configure --prefix=/usr \--disable-documentation && \  
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
  
USER nobody  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8388  
ENV PASSWORD 1234567890  
ENV METHOD chacha20  
ENV TIMEOUT 3600  
ENV DNS_ADDR 8.8.8.8  
ENV DNS_ADDR_2 8.8.4.4  
ENV OBFS_OPTS obfs=http;obfs-host=www.bing.com  
  
EXPOSE $SERVER_PORT/tcp  
EXPOSE $SERVER_PORT/udp  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

