#  
# Dockerfile for shadowsocks-libev  
#  
FROM alpine:edge  
MAINTAINER Lautis Sun <lautis0503@gmail.com>  
  
ENV NETSPEEDER_DEP libnet libpcap  
ENV NETSPEEDER_BUILD_DEP libnet-dev libpcap-dev  
ENV NETSPEEDER_URL https://github.com/snooda/net-speeder.git  
ENV NETSPEEDER_DIR net-speeder  
  
RUN set -ex \  
&& apk --no-cache --update add $NETSPEEDER_DEP $NETSPEEDER_BUILD_DEP  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
git \  
autoconf \  
automake \  
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
udns-dev  
  
# install net-speeder  
RUN set -ex \  
&& git clone $NETSPEEDER_URL $NETSPEEDER_DIR \  
&& cd $NETSPEEDER_DIR \  
&& sh build.sh \  
&& mv net_speeder /usr/local/bin/ \  
&& cd .. \  
&& rm -rf $NETSPEEDER_DIR \  
&& apk del --purge $NETSPEEDER_BUILD_DEP  
  
# install shadowsocks-libev  
RUN set -ex \  
&& git clone https://github.com/shadowsocks/shadowsocks-libev.git /usr/src/ss
\  
&& cd /usr/src/ss \  
&& git submodule update --init --recursive \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr --disable-documentation \  
&& make install \  
&& cd / \  
  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--no-cache --virtual .run-deps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /tmp/*  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8388  
ENV PASSWORD 1234567890  
ENV METHOD aes-256-cfb  
ENV TIMEOUT 3600  
ENV DNS_ADDR 8.8.8.8  
EXPOSE $SERVER_PORT/tcp  
EXPOSE $SERVER_PORT/udp  
  
COPY ./docker-entrypoint.sh /  
  
RUN chmod +x /usr/local/bin/net_speeder  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

