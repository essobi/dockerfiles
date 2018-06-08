  
# FROM ubuntu:latest  
# MAINTAINER nullun <nullun@null>  
# RUN apt-get update -y && apt-get install python-pip -y && pip install
shadowsocks  
  
FROM alpine:latest  
MAINTAINER nullun  
  
RUN apk update && apk add py-pip && pip install shadowsocks  
  
ENTRYPOINT ["/usr/bin/ssserver"]  
  
# FROM alpine:latest  
# MAINTAINER nullun  
  
# RUN set -ex \  
# && export SS_GIT=https://github.com/shadowsocks/shadowsocks-libev \  
# && export SS_DIR=shadowsocks-libev \  
# && apk upgrade --update \  
# && apk add --virtual .ss-builddeps git autoconf automake build-base libtool
linux-headers libressl-dev libsodium-dev udns-dev \  
# mbedtls-dev mbedtls-static libev-dev pcre-dev zlib-dev \  
# && apk add --virtual .ss-deps udns \  
# && git clone \--recursive $SS_GIT $SS_DIR \  
# && cd $SS_DIR \  
# && ./autogen.sh \  
# && ./configure --disable-documentation \  
# && make \  
# && cc src/ss_server*.o -Llibbloom/.libs/ -Llibcork/.libs/ -Llibipset/.libs/
\  
# -Wl,-Bstatic -lbloom -lipset -lcork -lsodium -lmbedcrypto -lpcre -lev \  
# -Wl,-Bdynamic -ludns -o src/ss-server-static \  
# && strip src/ss-server-static \  
# && install -m755 src/ss-server-static /usr/local/bin/ss-server \  
# && cd .. \  
# && rm -rf $SS_DIR \  
# && apk del --purge .ss-builddeps \  
# && rm -rf /var/cache/apk/*  

