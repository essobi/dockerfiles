#  
# Dockerfile for shadowsocks-libev  
#  
FROM alpine  
MAINTAINER kev <noreply@datageek.info>  
  
ARG SS_VER=3.1.1  
ARG SS_URL=https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz  
  
ENV MODULE ss-server  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8388  
ENV LOCAL_ADDR 0.0.0.0  
ENV LOCAL_PORT 1080  
ENV PASSWORD ""  
ENV METHOD aes-256-cfb  
ENV TIMEOUT 300  
ENV DNS_ADDR 8.8.8.8  
ENV DNS_ADDR_2 8.8.4.4  
ENV ARGS ""  
ENV USER nobody  
  
ENV OBFS http  
ENV OBFS_HOST www.bing.com  
  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
autoconf \  
build-base \  
curl \  
libev-dev \  
libtool \  
linux-headers \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
tar \  
c-ares-dev \  
git \  
gcc \  
make \  
libtool \  
automake \  
openssl \  
asciidoc \  
xmlto \  
libpcre32 \  
g++ && \  
  
cd /tmp && \  
curl -sSL $SS_URL | tar xz --strip 1 && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
cd .. && \  
  
rm -rf /tmp/* && \  
  
cd /tmp && \  
git clone https://github.com/shadowsocks/simple-obfs.git && \  
cd simple-obfs && \  
git submodule update --init --recursive && \  
./autogen.sh && \  
./configure && make && \  
make install && \  
  
runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
apk add \--no-cache --virtual .run-deps $runDeps && \  
apk del .build-deps && \  
rm -rf /tmp/*  
  
USER root  
  
EXPOSE $SERVER_PORT/tcp $SERVER_PORT/udp $LOCAL_PORT/tcp $LOCAL_PORT/udp  
  
ADD entrypoint.sh /  
RUN ["chmod", "+x", "/entrypoint.sh"]  
CMD ["/entrypoint.sh"]

