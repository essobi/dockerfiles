FROM alpine:3.5  
MAINTAINER mritd <mritd@mritd.me>  
  
ENV TZ 'Asia/Shanghai'  
ENV SS_LIBEV_VERSION 3.0.6  
ENV KCP_VERSION 20170329  
ENV SS_CONFIG "-s 0.0.0.0 -p 8288 -m aes-256-cfb -k testtest --fast-open"  
ENV SS_MODULE "ss-server"  
ENV KCP_CONFIG "-t 127.0.0.1:8288 -l :8300 -mode fast2"  
ENV KCP_FLAG "true"  
RUN apk upgrade --no-cache \  
&& apk add --no-cache bash tzdata libsodium \  
&& apk add --no-cache --virtual .build-deps \  
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
udns-dev \  
&& curl -sSLO https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_LIBEV_VERSION/shadowsocks-
libev-$SS_LIBEV_VERSION.tar.gz \  
&& tar -zxf shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \  
&& cd shadowsocks-libev-$SS_LIBEV_VERSION \  
&& ./configure --prefix=/usr --disable-documentation \  
&& make install && cd ../ \  
&& curl -sSLO
https://github.com/xtaci/kcptun/releases/download/v$KCP_VERSION/kcptun-linux-
amd64-$KCP_VERSION.tar.gz \  
&& tar -zxf kcptun-linux-amd64-$KCP_VERSION.tar.gz \  
&& mv server_linux_amd64 /usr/bin/kcptun \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .run-deps $runDeps \  
&& apk del .build-deps \  
&& rm -rf client_linux_amd64 \  
kcptun-linux-amd64-$KCP_VERSION.tar.gz \  
shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \  
shadowsocks-libev-$SS_LIBEV_VERSION \  
/var/cache/apk/*  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod -R 755 /entrypoint.sh  
  
EXPOSE 8288  
EXPOSE 8300  
ENTRYPOINT ["/entrypoint.sh"]

