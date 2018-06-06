FROM alpine:3.7  
  
ENV TZ 'Asia/Shanghai'  
  
ENV SS_LIBEV_VERSION 3.1.3  
  
ENV KCP_VERSION 20180316  
  
RUN \  
set -ex \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
autoconf \  
build-base \  
libtool \  
linux-headers \  
libressl-dev \  
zlib-dev \  
asciidoc \  
xmlto \  
pcre-dev \  
automake \  
mbedtls-dev \  
libsodium-dev \  
c-ares-dev \  
libev-dev \  
&& apk add --no-cache --virtual .run-deps \  
pcre \  
libev \  
c-ares \  
libsodium \  
mbedtls \  
&& curl -sSLO https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_LIBEV_VERSION/shadowsocks-
libev-$SS_LIBEV_VERSION.tar.gz \  
&& tar -zxf shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \  
&& cd shadowsocks-libev-$SS_LIBEV_VERSION \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& curl -sSLO
https://github.com/xtaci/kcptun/releases/download/v$KCP_VERSION/kcptun-linux-
amd64-$KCP_VERSION.tar.gz \  
&& tar -zxf kcptun-linux-amd64-$KCP_VERSION.tar.gz \  
&& mv server_linux_amd64 /usr/bin/server_linux_amd64 \  
&& mv client_linux_amd64 /usr/bin/client_linux_amd64 \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .run-deps $runDeps \  
&& apk del .build-deps \  
&& apk add --no-cache privoxy \  
&& rm -rf kcptun-linux-amd64-$KCP_VERSION.tar.gz \  
shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \  
shadowsocks-libev-$SS_LIBEV_VERSION \  
/var/cache/apk/*  
ADD kcp2ss-server.sh /kcp2ss-server.sh  
ADD ss2kcp-client.sh /ss2kcp-client.sh  
ADD ss-local.sh /ss-local.sh  
ADD ss-server.sh /ss-server.sh  
ADD p2ss2kcp-client.sh /p2ss2kcp-client.sh  
ADD kcp-client.sh /kcp-client.sh  
ADD kcp-server.sh /kcp-server.sh  
RUN chmod +x /*.sh  
  
  
  

