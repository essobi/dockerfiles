FROM alpine:3.7  
ENV LIBSODIUM_VER 1.0.13  
ENV MBEDTLS_VER 2.6.0  
ENV SS_LIBEV_VERSION 3.1.3  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8388  
ENV PASSWORD 12345678  
ENV METHOD aes-256-cfb  
ENV TIMEOUT 600  
ENV ARGS=  
  
RUN apk add --update --no-cache --virtual .build-deps \  
autoconf \  
automake \  
curl \  
build-base \  
c-ares-dev \  
libev-dev \  
libtool \  
linux-headers \  
pcre-dev \  
&& mkdir /tmp/repo \  
&& cd /tmp/repo \  
&& curl -sSLO
https://download.libsodium.org/libsodium/releases/libsodium-$LIBSODIUM_VER.tar.gz
\  
&& tar xvf libsodium-$LIBSODIUM_VER.tar.gz \  
&& cd libsodium-$LIBSODIUM_VER \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install  
#  
RUN cd /tmp/repo \  
&& curl -sSLO https://tls.mbed.org/download/mbedtls-$MBEDTLS_VER-gpl.tgz \  
&& tar xvf mbedtls-$MBEDTLS_VER-gpl.tgz \  
&& cd mbedtls-$MBEDTLS_VER \  
&& make SHARED=1 CFLAGS=-fPIC \  
&& make DESTDIR=/usr install  
#  
RUN cd /tmp/repo \  
&& curl -sSLO https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_LIBEV_VERSION/shadowsocks-
libev-$SS_LIBEV_VERSION.tar.gz \  
&& tar -zxf shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \  
&& cd shadowsocks-libev-$SS_LIBEV_VERSION \  
&& ./configure --prefix=/usr --disable-documentation \  
&& make install  
  
RUN apk del .build-deps  
#  
RUN apk add --no-cache \  
rng-tools \  
$(scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| sed '/sodium/d' \  
| sed '/mbedcrypto/d')  
#  
RUN rm -rf /tmp/repo  
  
CMD exec ss-server \  
-s $SERVER_ADDR \  
-p $SERVER_PORT \  
-k ${PASSWORD:-$(hostname)} \  
-m $METHOD \  
-t $TIMEOUT \  
-u \  
$ARGS  

