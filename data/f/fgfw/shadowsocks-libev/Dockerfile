#  
# Dockerfile for shadowsocks-libev  
#  
  
FROM alpine:3.3  
MAINTAINER Li ZHOU  
  
ENV SS_VER 2.5.0  
ENV SS_URL https://github.com/shadowsocks/shadowsocks-
libev/archive/v$SS_VER.tar.gz  
ENV SS_DIR shadowsocks-libev-$SS_VER  
  
RUN set -ex \  
&& apk add --no-cache libcrypto1.0 \  
libev \  
libsodium \  
pcre \  
udns \  
&& apk add --no-cache \  
\--virtual TMP autoconf \  
automake \  
build-base \  
curl \  
file \  
gettext-dev \  
libev-dev \  
libsodium-dev \  
libtool \  
linux-headers \  
openssl-dev \  
pcre-dev \  
tar \  
udns-dev \  
&& curl -sSL $SS_URL | tar xz \  
&& cd $SS_DIR \  
&& curl -sSL https://github.com/shadowsocks/ipset/archive/shadowsocks.tar.gz |
tar xz --strip 1 -C libipset \  
&& curl -sSL https://github.com/shadowsocks/libcork/archive/shadowsocks.tar.gz
| tar xz --strip 1 -C libcork \  
&& ./autogen.sh \  
&& ./configure \--disable-documentation \  
&& make install \  
&& cd .. \  
&& rm -rf $SS_DIR \  
&& apk del TMP  
  
ENV SERVER_ADDR 127.0.0.1  
ENV SERVER_PORT 1491  
ENV METHOD camellia-128-cfb  
ENV PASSWORD easy3.14  
  
EXPOSE $SERVER_PORT/tcp  
  
CMD ss-server -s "$SERVER_ADDR" -p "$SERVER_PORT" -m "$METHOD" -k "$PASSWORD"  

