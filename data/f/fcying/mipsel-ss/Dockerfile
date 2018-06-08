FROM ubuntu:16.04  
MAINTAINER fcying  
  
WORKDIR /mnt  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
g++-mipsel-linux-gnu gcc-mipsel-linux-gnu \  
gettext build-essential autoconf libtool libpcre3-dev asciidoc xmlto \  
libev-dev libc-ares-dev automake libmbedtls-dev libsodium-dev \  
wget git ca-certificates openssl  
  
RUN ver=1.0.13 \  
&& wget --no-check-certificate
https://download.libsodium.org/libsodium/releases/libsodium-$ver.tar.gz \  
&& tar zxf libsodium-$ver.tar.gz \  
&& cd libsodium-$ver \  
&& ./configure --host=mipsel-linux-gnu --prefix=/opt/libsodium --disable-ssp
--disable-shared \  
&& make && make install  
  
RUN ver=2.6.0 \  
&& wget --no-check-certificate https://tls.mbed.org/download/mbedtls-$ver-
gpl.tgz \  
&& tar zxf mbedtls-$ver-gpl.tgz \  
&& cd mbedtls-$ver \  
&& sed -i "s/DESTDIR=\/usr\/local/DESTDIR=\/opt\/mbedtls/g" Makefile \  
&& CC=mipsel-linux-gnu-gcc AR=mipsel-linux-gnu-ar LD=mipsel-linux-gnu-ld
LDFLAGS=-static make install  
  
RUN ver=8.41 \  
&& wget --no-check-certificate https://ftp.pcre.org/pub/pcre/pcre-$ver.tar.gz
\  
&& tar zxf pcre-$ver.tar.gz \  
&& cd pcre-$ver \  
&& ./configure --host=mipsel-linux-gnu --prefix=/opt/pcre --disable-shared
--enable-utf8 --enable-unicode-properties \  
&& make && make install  
  
RUN ver=4.24 \  
&& wget http://dist.schmorp.de/libev/libev-$ver.tar.gz \  
&& tar zxf libev-$ver.tar.gz \  
&& cd libev-$ver \  
&& ./configure --host=mipsel-linux-gnu --prefix=/opt/libev --disable-shared \  
&& make && make install  
  
RUN ver=1_13_0 \  
&& wget --no-check-certificate
https://github.com/c-ares/c-ares/archive/cares-$ver.tar.gz \  
&& tar xzf cares-$ver.tar.gz \  
&& cd c-ares-cares-$ver \  
&& ./buildconf \  
&& ./configure --host=mipsel-linux-gnu LDFLAGS=-static --prefix=/opt/c-ares \  
&& make && make install  
  
COPY myinit /bin  
RUN chmod 700 /bin/myinit \  
&& mkdir /ss \  
&& export ver=3.1.3 \  
&& rm -rf /mnt/* \  
&& git clone https://github.com/shadowsocks/shadowsocks-libev \  
&& /bin/myinit update  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/bin/myinit"]  

