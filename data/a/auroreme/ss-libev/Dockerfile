FROM alpine:latest  
  
ARG PCRE_VERSION=8.41  
ARG CARES_VERSION=1.14.0  
ARG SODIUM_VERSION=1.0.16  
ARG MBEDTLS_VERSION=2.7.0  
  
RUN apk add \--no-cache rng-tools  
  
RUN apk add \--no-cache \  
\--virtual .build-deps \  
git \  
tar \  
curl \  
file \  
libtool \  
autoconf \  
automake \  
build-base \  
linux-headers \  
&& mkdir .build-dir && cd .build-dir \  
&& mkdir pcre c-ares mbedtls libsodium \  
&& git clone \--depth=1 https://github.com/shadowsocks/libev.git \  
&& git clone \--depth=1 https://github.com/shadowsocks/shadowsocks-libev.git \  
&& curl -sSL https://ftp.pcre.org/pub/pcre/pcre-${PCRE_VERSION}.tar.gz | tar
xz \--strip 1 -C pcre \  
&& curl -sSL https://c-ares.haxx.se/download/c-ares-${CARES_VERSION}.tar.gz |
tar xz \--strip 1 -C c-ares \  
&& curl -sSL
https://tls.mbed.org/download/mbedtls-${MBEDTLS_VERSION}-apache.tgz | tar xz
\--strip 1 -C mbedtls \  
&& curl -sSL
https://github.com/jedisct1/libsodium/releases/download/${SODIUM_VERSION}/libsodium-${SODIUM_VERSION}.tar.gz
| tar xz \--strip 1 -C libsodium \  
&& cd pcre \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& cd libev \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& cd c-ares \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& cd mbedtls \  
&& make \  
&& make install \  
&& cd .. \  
&& cd libsodium \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& ldconfig -n /usr/local/lib \  
&& cd shadowsocks-libev \  
&& git submodule update \--init \--recursive \  
&& ./autogen.sh \  
&& ./configure \--disable-documentation \  
&& make \  
&& make install \  
&& cd .. \  
&& cd .. \  
&& rm -rf .build-dir \  
&& apk del .build-deps  
  
COPY config.json /etc/shadowsocks/config.json  
COPY banLAN.acl /etc/shadowsocks/banLAN.acl  
  
CMD ["ss-server", "-c", "/etc/shadowsocks/config.json", "--acl",
"/etc/shadowsocks/banLAN.acl"]  

