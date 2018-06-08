  
FROM alpine:3.4  
  
ENV SSversion 3.0.6  
ENV SSfilename shadowsocks-libev-3.0.6.tar.gz  
  
RUN apk upgrade --no-cache \  
&& apk add --no-cache --virtual .build-deps \  
autoconf \  
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
udns-dev \  
&& cd /tmp \  
&& curl -sSLO https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SSversion/shadowsocks-libev-$SSversion.tar.gz \  
&& tar -zxf shadowsocks-libev-$SSversion.tar.gz \  
&& cd shadowsocks-libev-$SSversion \  
&& ./configure --prefix=/usr --disable-documentation \  
&& make install  

