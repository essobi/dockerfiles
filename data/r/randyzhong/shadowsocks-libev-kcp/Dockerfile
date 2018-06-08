# Docker Image - Shadowsocks + KCP  
# VERSION 1.0  
# Use Alpine Linux as the base image  
FROM alpine:latest  
  
# Maintainer Information  
LABEL maintainer "noreply@randyzhong.me"  
# Define Shadowsocks-libev version  
ARG SS_LIBEV_VERSION=3.1.3  
ARG SS_LIBEV_URL=https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v${SS_LIBEV_VERSION}/shadowsocks-
libev-${SS_LIBEV_VERSION}.tar.gz  
  
# Define KCPTUN version  
ARG KCP_VERSION=20171201  
ARG
KCP_URL=https://github.com/xtaci/kcptun/releases/download/v${KCP_VERSION}/kcptun-
linux-amd64-${KCP_VERSION}.tar.gz  
  
# Define TimeZone  
ARG TIMEZONE=Asia/Shanghai  
  
# Install dependencies  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
autoconf \  
build-base \  
curl \  
libev-dev \  
libtool \  
linux-headers \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
tar \  
tzdata \  
c-ares-dev \  
&& cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
&& cd /tmp \  
&& curl -sSL ${KCP_URL} | tar xz server_linux_amd64 \  
&& mv server_linux_amd64 /usr/bin/ \  
&& curl -sSL ${SS_LIBEV_URL} | tar xz --strip 1 \  
&& ./configure --prefix=/usr --disable-documentation \  
&& make install \  
&& cd ../ \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .run-deps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /tmp/* \  
/var/cache/apk/*  
  
# Define Shadowsocks and KCP Ports  
ENV SS_SERVER_ADDR=${SS_SERVER_ADDR:-0.0.0.0} \  
SS_SERVER_PORT=${SS_SERVER_PORT:-5020} \  
SS_PASSWORD=${SS_PASSWORD:-secret} \  
SS_METHOD=$(SS_METHOD:-aes-256-cfb} \  
SS_TIMEOUT=${SS_TIMEOUT:-300} \  
SS_DNS_ADDR1=$(SS_DNS_ADDR1:-8.8.8.8} \  
SS_DNS_ADDR2=$(SS_DNS_ADDR1:-8.8.4.4} \  
KCP_PORT=${KCP_PORT:-5021} \  
KCP_KEY=${KCP_KEY:-kcptun} \  
KCP_MODE=${KCP_MODE:-fast} \  
KCP_CRYPT=${KCP_CRYPT:-salsa20} \  
KCP_MTU=${KCP_MTU:-1350} \  
KCP_DSCP=${KCP_DSCP:-46}  
  
USER nobody  
  
# Expose Shadowsocker & KCP port  
EXPOSE ${SS_SERVER_PORT}/tcp ${SS_SERVER_PORT}/udp  
EXPOSE ${KCP_PORT}/udp  
  
# Start Services  
CMD ss-server -s $SS_SERVER_ADDR \  
-p $SS_SERVER_PORT \  
-k $SS_PASSWORD \  
-m $SS_METHOD \  
-t $SS_TIMEOUT \  
\--fast-open \  
-d $SS_DNS_ADDR1 \  
-d $SS_DNS_ADDR2 \  
-u \  
&& server_linux_amd64 -t 127.0.0.1:$SS_SERVER_PORT \  
-l :$KCP_PORT \  
\--key $KCP_KEY \  
\--mode $KCP_MODE \  
\--crypt $KCP_CRYPT \  
\--mtu $KCP_MTU \  
\--dscp $KCP_DSCP \  
\--nocomp  

