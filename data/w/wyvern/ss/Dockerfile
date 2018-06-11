#  
# Dockerfile for shadowsocks-libev  
#  
FROM alpine  
MAINTAINER EasyPi Software Foundation  
  
ENV SS_VER 2.6.2  
ENV SS_URL https://github.com/shadowsocks/shadowsocks-
libev/archive/v$SS_VER.tar.gz  
ENV SS_DIR shadowsocks-libev-$SS_VER  
  
RUN set -ex \  
&& apk add --no-cache libcrypto1.0 pcre \  
&& apk add --no-cache \  
\--virtual TMP autoconf \  
build-base \  
curl \  
libtool \  
linux-headers \  
openssl-dev \  
pcre-dev \  
&& curl -sSL $SS_URL | tar xz \  
&& cd $SS_DIR \  
&& ./configure --disable-documentation \  
&& make install \  
&& cd .. \  
&& rm -rf $SS_DIR \  
&& apk del TMP  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 443  
ENV METHOD rc4-md5  
ENV PASSWORD asdfjkl  
ENV TIMEOUT 60  
ENV DNS_ADDR 8.8.8.8  
EXPOSE $SERVER_PORT/tcp  
EXPOSE $SERVER_PORT/udp  
  
CMD ss-server -s "$SERVER_ADDR" \  
-p "$SERVER_PORT" \  
-m "$METHOD" \  
-k "$PASSWORD" \  
-t "$TIMEOUT" \  
-d "$DNS_ADDR" \  
-u \  
-A \  
\--fast-open $OPTIONS  

