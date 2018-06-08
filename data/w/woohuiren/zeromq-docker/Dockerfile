FROM alpine:3.5  
  
LABEL maintainer="Huiren Woo <giantcrabby@gmail.com>" \  
alpine="3.5" \  
libsodium="1.0.12" \  
libzmq="4.2.2"  
  
RUN BUILD_DEPENDENCIES="build-base \  
libtool \  
automake \  
autoconf" \  
DEV_DEPENDENCIES="unzip \  
libunwind-dev \  
krb5-dev" \  
&& apk update && apk upgrade -U -a && apk add \  
git \  
$BUILD_DEPENDENCIES \  
$DEV_DEPENDENCIES \  
&& cd /tmp && git clone git://github.com/jedisct1/libsodium.git && cd
libsodium && git checkout 70170c2 && ./autogen.sh && ./configure && make check
&& make install && ldconfig \  
&& cd /tmp && git clone git://github.com/zeromq/libzmq.git && cd libzmq && git
checkout 8d75d50 && ./autogen.sh && ./configure && make && make check && make
install && ldconfig \  
&& rm /tmp/* -rf \  
&& apk del --purge $BUILD_DEPENDENCIES

