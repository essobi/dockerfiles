# Shadowsocks Server with KCPTUN support Dockerfile  
FROM alpine:3.4  
ENV SS_VER 2.5.5  
ENV KCP_VER 20161105  
RUN \  
apk add --no-cache --virtual .build-deps \  
curl \  
autoconf \  
build-base \  
libtool \  
linux-headers \  
openssl-dev \  
asciidoc \  
xmlto \  
pcre-dev \  
&& apk add --no-cache --virtual .run-deps \  
pcre \  
&& curl -fSL https://github.com/shadowsocks/shadowsocks-
libev/archive/v$SS_VER.tar.gz | tar xz \  
&& cd shadowsocks-libev-$SS_VER \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf shadowsocks-libev-$SS_VER \  
&& mkdir -p /opt/kcptun \  
&& cd /opt/kcptun \  
&& curl -fSL
https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-linux-
amd64-$KCP_VER.tar.gz | tar xz \  
&& rm client_linux_amd64  
#&& apk del .build-deps  
ENV SS_PORT=443  
ENV KCP_PORT=29900  
EXPOSE $SS_PORT/tcp $SS_PORT/udp $KCP_PORT/udp  
  
ENTRYPOINT ss-server -p 443 -k $SS_PASSWORD -m chacha20 -t 600 -d 8.8.8.8 -d
208.67.222.222 -u --fast-open  

