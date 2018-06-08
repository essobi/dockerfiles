# ShadownSock Libev with Ubuntu  
#  
# VERSION 1.1.0  
FROM ubuntu:16.04  
MAINTAINER FrankZhang "zjufrankzhang@gmail.com"  
ENV DEPENDENCIES git-core gettext automake build-essential autoconf libtool
libssl-dev libpcre3-dev asciidoc xmlto zlib1g-dev libsodium-dev libmbedtls-dev
libev-dev libudns-dev ca-certificates wget  
ENV BASEDIR /tmp/shadowsocks-libev  
ENV LIBDIR /tmp/ss-libs  
ENV VERSION v3.0.2  
ENV LIBSODIUM_VER 1.0.11  
ENV MBEDTLS_VER 2.4.0  
# Set up building environment  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends $DEPENDENCIES  
  
# Build and install with recent mbedTLS and libsodium  
WORKDIR $LIBDIR  
RUN wget
https://github.com/jedisct1/libsodium/releases/download/1.0.11/libsodium-$LIBSODIUM_VER.tar.gz  
RUN tar xvf libsodium-$LIBSODIUM_VER.tar.gz  
WORKDIR $LIBDIR/libsodium-$LIBSODIUM_VER  
RUN ./configure --prefix=/usr && make && make install  
  
WORKDIR $LIBDIR  
RUN wget https://tls.mbed.org/download/mbedtls-$MBEDTLS_VER-gpl.tgz  
RUN tar xvf mbedtls-$MBEDTLS_VER-gpl.tgz  
WORKDIR $LIBDIR/mbedtls-$MBEDTLS_VER  
RUN make SHARED=1 CFLAGS=-fPIC  
RUN make DESTDIR=/usr install  
  
# Get the latest code, build and install  
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git $BASEDIR  
WORKDIR $BASEDIR  
RUN git submodule init && git submodule update  
RUN git checkout $VERSION \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
# Tear down building environment and delete git repository  
WORKDIR /  
RUN rm -rf $BASEDIR\  
&& rm -rf $LIBDIR  
  
# easier to configure and integrate passwords  
ADD config.json /etc/shadowsocks-libev/config.json  
  
# Use Data Volume to manage config  
VOLUME ["/etc/shadowsocks-libev/"]  
  
# Note: we need to clearly expose the port number.  
# Run it: thanks to entrypoint, we can add options when launching the
container  
ENTRYPOINT ["/usr/local/bin/ss-server"]  
CMD ["-c", "/etc/shadowsocks-libev/config.json", "-u"]  

