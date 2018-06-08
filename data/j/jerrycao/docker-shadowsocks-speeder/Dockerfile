#  
# Dockerfile for shadowsocks-libev  
#  
FROM alpine:edge  
MAINTAINER Tony.Shao <xiocode@gmail.com>  
  
ENV SS_VERSION v2.5.2  
ENV SS_URL https://github.com/shadowsocks/shadowsocks-libev.git  
ENV SS_DIR shadowsocks-libev  
ENV SS_DEP pcre  
ENV SS_BUILD_DEP git autoconf build-base curl libtool linux-headers openssl-
dev asciidoc xmlto pcre-dev  
  
ENV NETSPEEDER_DEP libnet libpcap  
ENV NETSPEEDER_BUILD_DEP libnet-dev libpcap-dev  
ENV NETSPEEDER_URL https://github.com/snooda/net-speeder.git  
ENV NETSPEEDER_DIR net-speeder  
  
RUN set -ex \  
&& apk --no-cache --update add $SS_DEP $SS_BUILD_DEP $NETSPEEDER_DEP
$NETSPEEDER_BUILD_DEP  
  
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
&& git clone $SS_URL \  
&& cd $SS_DIR \  
&& git checkout tags/$SS_VERSION \  
&& ./configure \  
&& make install \  
&& cd .. \  
&& rm -rf $SS_DIR \  
&& apk del --purge $SS_BUILD_DEP \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8388  
ENV PASSWORD 1234567890  
ENV METHOD chacha20  
ENV TIMEOUT 3600  
ENV DNS_ADDR 8.8.8.8  
EXPOSE $SERVER_PORT/tcp  
EXPOSE $SERVER_PORT/udp  
  
COPY ./docker-entrypoint.sh /  
  
RUN chmod +x /usr/local/bin/net_speeder  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

