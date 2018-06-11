FROM pipill/armhf-alpine  
  
ENV SS_VER=3.0.8  
ENV SS_URL=https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz  
  
ENV SIMPLE_OBFS_VER=0.0.3  
  
RUN [ "cross-build-start" ]  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
autoconf \  
automake \  
build-base \  
curl \  
libev-dev \  
libtool \  
linux-headers \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
tar \  
git \  
udns-dev && \  
cd /tmp && \  
git clone --depth=1 https://github.com/shadowsocks/simple-obfs.git . && \  
git submodule update --init --recursive && \  
./autogen.sh && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
rm -rf * && \  
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
apk add --no-cache --virtual .run-deps $runDeps && \  
apk del .build-deps && \  
rm -rf /tmp/*  
  
  
RUN apk --update --no-cache add bash iptables ipset curl \  
&& sed -i 's/${IFNAME:+-i $IFNAME} //g' /usr/bin/ss-nat \  
&& curl 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest' | grep
ipv4 | grep CN | awk -F\| '{ printf("%s/%d\n", $4, 32-log($5)/log(2)) }' >
/chnroute.txt  
RUN [ "cross-build-end" ]  
#VOLUME ["/chnroute.txt"]  
  
ENV SS_SERVER_IP= \  
SS_SERVER_PORT=8388 \  
SS_METHOD=chacha20-ietf-poly1305 \  
SS_PASSWD= \  
SS_LOCAL_PORT=1080 \  
SS_TIMEOUT=300 \  
SS_ARGS=  
  
COPY ss-wrapper /usr/bin/  
CMD ["/usr/bin/ss-wrapper"]  

