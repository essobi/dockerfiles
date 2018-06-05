FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
MAINTAINER XUTONGLE <xutongle@gmail.com>  
  
ADD entrypoint.sh /root/entrypoint.sh  
  
RUN apt-get update && apt-get install -y gettext build-essential autoconf
libtool libpcre3-dev asciidoc libev-dev \  
libc-ares-dev automake xmlto curl --no-install-recommends && rm -r
/var/lib/apt/lists/* && chmod 700 /root/entrypoint.sh  
  
ARG SS_VERSION=3.1.3  
ENV SS_DIR=/usr/local \  
MBEDTLS_VER=2.6.0 \  
LIBSODIUM_VER=1.0.15 \  
SS_PASSWORD="123456" \  
SS_PORT=1080 \  
SS_METHOD="aes-256-cfb" \  
SS_TIMEOUT=300 \  
SS_FAST_OPEN="--fast-open"  
RUN cd /usr/local/src && curl -k -o libsodium-${LIBSODIUM_VER}.tar.gz
https://download.libsodium.org/libsodium/releases/libsodium-${LIBSODIUM_VER}.tar.gz
&& \  
tar xvf libsodium-${LIBSODIUM_VER}.tar.gz && rm -rf
libsodium-${LIBSODIUM_VER}.tar.gz && cd libsodium-${LIBSODIUM_VER} && \  
./configure --prefix=/usr && make && make install && ldconfig && \  
rm -rf /usr/local/src/libsodium-${LIBSODIUM_VER}  
  
RUN cd /usr/local/src && curl -k -o mbedtls-${MBEDTLS_VER}-gpl.tgz
https://tls.mbed.org/download/mbedtls-${MBEDTLS_VER}-gpl.tgz && \  
tar xvf mbedtls-${MBEDTLS_VER}-gpl.tgz && rm -rf
mbedtls-${MBEDTLS_VER}-gpl.tgz && cd mbedtls-${MBEDTLS_VER} && \  
make SHARED=1 CFLAGS=-fPIC && make DESTDIR=/usr install && ldconfig && \  
rm -rf /usr/local/src/mbedtls-${MBEDTLS_VER}  
  
RUN cd /usr/local/src && curl -L -k -o shadowsocks-libev-${SS_VERSION}.tar.gz
https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v${SS_VERSION}/shadowsocks-libev-${SS_VERSION}.tar.gz
&& \  
tar zxf shadowsocks-libev-${SS_VERSION}.tar.gz && rm -rf shadowsocks-
libev-${SS_VERSION}.tar.gz && cd shadowsocks-libev-${SS_VERSION}/ && \  
./configure --prefix=/usr --disable-documentation && make && make install &&
rm -rf /usr/local/src/shadowsocks-libev-${SS_VERSION}  
  
# Define the default command.  
ENTRYPOINT ["/root/entrypoint.sh"]  

