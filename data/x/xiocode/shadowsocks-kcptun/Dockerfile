#  
# Dockerfile for shadowsocks-libev  
#  
FROM alpine:edge  
MAINTAINER Tony.Shao <xiocode@gmail.com>  
  
ENV SS_VERSION v2.5.6  
ENV SS_URL https://github.com/shadowsocks/shadowsocks-libev.git  
ENV SS_DIR shadowsocks-libev  
ENV SS_DEP pcre  
ENV SS_BUILD_DEP git autoconf build-base curl libtool linux-headers openssl-
dev asciidoc xmlto pcre-dev  
  
ENV KCPTUN_VERSION 20161111  
ENV KCPTUN_FILE kcptun-linux-amd64-${KCPTUN_VERSION}.tar.gz  
ENV KCPTUN_URL
https://github.com/xtaci/kcptun/releases/download/v${KCPTUN_VERSION}/${KCPTUN_FILE}  
  
RUN set -ex \  
&& apk --no-cache --update add supervisor  
  
ADD supervisord.conf /etc/supervisord.conf  
  
RUN set -ex \  
&& apk --no-cache --update add $SS_DEP $SS_BUILD_DEP \  
&& git clone $SS_URL \  
&& cd $SS_DIR \  
&& git checkout tags/$SS_VERSION \  
&& ./configure \  
&& make install \  
&& cd .. \  
&& rm -rf $SS_DIR  
  
RUN set -ex \  
&& curl -sSL ${KCPTUN_URL} | tar xz -C /usr/local/bin  
  
RUN set -ex \  
&& apk del --purge $SS_BUILD_DEP \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
ENV SS_PORT 7777  
ENV SS_PASSWORD 1234567890  
ENV SS_METHOD rc4-md5  
  
ENV KCP_TARGET 127.0.0.1:7777  
ENV KCP_PORT 8888  
ENV KCP_CRYPT salsa20  
ENV KCP_KEY 1234567890  
ENV KCP_SEND_WINDOW 2048  
ENV KCP_RECEIVE_WINDOW 2048  
ENV KCP_MTU 1400  
ENV KCP_DATASHARD 70  
ENV KCP_PARITYSHARD 30  
ENV KCP_INTERVAL 50  
ENV KCP_NODELAY 0  
ENV KCP_RESEND 0  
ENV KCP_NC 0  
ENV KCP_ACKNODELAY true  
ENV KCP_NOCOMP false  
ENV KCP_SOCKBUF 4194304  
ENV KCP_DSCP 0  
ENV KCP_MODE fast2  
  
  
EXPOSE $SS_PORT  
EXPOSE $KCP_PORT  
  
CMD ["supervisord", "-n"]  

