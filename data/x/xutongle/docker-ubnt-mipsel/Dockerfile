FROM ubuntu:16.04  
  
MAINTAINER XUTONGLE <xutongle@gmail.com>  
  
WORKDIR /app  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
g++-mipsel-linux-gnu gcc-mipsel-linux-gnu \  
gettext build-essential autoconf libtool libpcre3-dev asciidoc xmlto \  
libev-dev libc-ares-dev automake libmbedtls-dev libsodium-dev \  
wget git ca-certificates openssl && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
## libsodium  
wget \--no-check-certificate
https://download.libsodium.org/libsodium/releases/libsodium-1.0.15.tar.gz && \  
tar zxf libsodium-1.0.15.tar.gz && cd libsodium-1.0.15 && \  
./configure \--host=mipsel-linux-gnu \--prefix=/opt/libsodium \--disable-ssp
\--disable-shared && \  
make && make install && \  
cd /app/ && \  
  
## pcre  
wget -c \--no-check-certificate https://ftp.pcre.org/pub/pcre/pcre-8.41.tar.gz
&& \  
tar xzf pcre-8.41.tar.gz && cd pcre-8.41 && \  
./configure \--prefix=/opt/pcre \--host=mipsel-linux-gnu \--disable-shared
\--enable-utf \--enable-unicode-properties && \  
make && make install && \  
cd /app/ && \  
  
# libev  
wget http://dist.schmorp.de/libev/libev-4.24.tar.gz && \  
tar zxf libev-4.24.tar.gz && cd libev-4.24 && \  
./configure \--host=mipsel-linux-gnu \--prefix=/opt/libev \--disable-shared &&
\  
make && make install && \  
cd /app/ && \  
  
# cares  
wget \--no-check-certificate
https://github.com/c-ares/c-ares/archive/cares-1_13_0.tar.gz && \  
tar xzf cares-1_13_0.tar.gz && cd c-ares-cares-1_13_0 && ./buildconf && \  
./configure \--host=mipsel-linux-gnu LDFLAGS=-static \--prefix=/opt/c-ares &&
\  
make && make install && \  
cd /app/ && \  
  
# mbedtls  
wget \--no-check-certificate
https://tls.mbed.org/download/mbedtls-2.6.0-gpl.tgz && \  
tar zxf mbedtls-2.6.0-gpl.tgz && cd mbedtls-2.6.0 && \  
sed -i "s/DESTDIR=\/usr\/local/DESTDIR=\/opt\/mbedtls/g" Makefile && \  
CC=mipsel-linux-gnu-gcc AR=mipsel-linux-gnu-ar LD=mipsel-linux-gnu-ld
LDFLAGS=-static make install && \  
cd /app/ && rm -rf /app \  

