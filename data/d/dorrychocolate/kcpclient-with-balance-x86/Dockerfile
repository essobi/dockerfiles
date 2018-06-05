FROM alpine:3.4  
# build shadowsocks-libev  
ENV SS_VER 3.0.3  
ENV SS_URL https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz  
RUN set -ex && \  
apk add --update --no-cache --virtual .build-deps \  
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
udns-dev && \  
cd /tmp && \  
curl -sSL $SS_URL | tar xz --strip 1 && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
cd .. && \  
  
runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
apk add \--no-cache --virtual .run-deps $runDeps && \  
apk del .build-deps && \  
rm -rf /tmp/* && \  
apk add --update bash  
  
ENV PEN_VER 0.34.1  
ENV PEN_URL http://siag.nu/pub/pen/pen-$PEN_VER.tar.gz  
ENV PEN_DIR /pen-$PEN_VER  
ENV PEN_DEP build-base autoconf automake gcc make  
  
ENV KCP_VER 20180316  
ENV KCP_URL
https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-linux-
amd64-$KCP_VER.tar.gz  
  
  
RUN apk update && \  
apk upgrade && \  
# get general dependency  
apk add \--update bash curl python openssl-dev && \  
# get kcpclient  
curl -sSL "$KCP_URL" | tar -xvzC /bin/ && \  
# get pen source code  
curl -sSL "$PEN_URL" | tar -xvz && \  
# clean general dependency  
apk del --purge curl openssl-dev  
  
  
# build pen  
WORKDIR "$PEN_DIR"  
RUN apk add --update $PEN_DEP && \  
aclocal && \  
automake --add-missing && \  
autoconf && \  
./configure && \  
make install && \  
# clear build dependency  
apk del --purge $PEN_DEP && \  
rm -rf /var/cache/apk/*  
  
# clean build dependency  
WORKDIR /  
RUN rm -rf $PEN_DIR  
ADD init ./  
ENTRYPOINT ./init  

