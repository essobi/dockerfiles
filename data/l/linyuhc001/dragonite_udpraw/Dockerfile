FROM alpine:3.7  
  
ARG TZ='Asia/Shanghai'  
  
ENV TZ $TZ  
ENV SS_LIBEV_VERSION 3.1.3  
ENV RAW_VERSION 20171125.0  
  
RUN apk upgrade --update \  
&& apk add bash tzdata libsodium openjdk8-jre-base iptables \  
&& apk add --virtual .build-deps \  
autoconf \  
automake \  
asciidoc \  
xmlto \  
build-base \  
curl \  
libev-dev \  
libtool \  
c-ares-dev \  
linux-headers \  
udns-dev \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
udns-dev \  
tar \  
git \  
&& curl -sSLO https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_LIBEV_VERSION/shadowsocks-
libev-$SS_LIBEV_VERSION.tar.gz \  
&& tar -zxf shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \  
&& (cd shadowsocks-libev-$SS_LIBEV_VERSION \  
&& ./configure --prefix=/usr --disable-documentation \  
&& make install ) \  
&& curl -sSLO https://github.com/dragonite-network/dragonite-
java/releases/download/fwd-0.3.3-prx-0.3.1/dragonite-forwarder-0.3.3.tar \  
&& mkdir /dragonite \  
&& tar -xvf dragonite-forwarder-0.3.3.tar -C /dragonite \  
&& chmod +x /dragonite/dragonite-forwarder-0.3.3/bin/dragonite-forwarder \  
&& curl -sSLO https://github.com/wangyu-/udp2raw-
tunnel/releases/download/$RAW_VERSION/udp2raw_binaries.tar.gz \  
&& tar -zxf udp2raw_binaries.tar.gz \  
&& mv udp2raw_amd64 /usr/bin/udpraw \  
&& ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .run-deps $runDeps \  
&& apk del .build-deps \  
&& rm -rf dragonite-forwarder-0.3.3.tar \  
shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \  
shadowsocks-libev-$SS_LIBEV_VERSION \  
udp2raw_binaries.tar.gz \  
/var/cache/apk/*  
  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

