FROM golang:alpine  
  
COPY main.go /go/src/github.com/9seconds/docker-shadow/main.go  
  
RUN set -ex \  
&& cd /go/src/github.com/9seconds/docker-shadow \  
&& env CGO_ENABLED=0 GOOS=linux GOARCH=amd64 \  
go build -a -installsuffix cgo -ldflags="-s -w" -o /entry  
  
#
-----------------------------------------------------------------------------  
  
FROM shadowsocks/shadowsocks-libev  
  
USER root  
ENTRYPOINT ["/entry"]  
ENV LD_PRELOAD=/lib/runit-docker.so  
EXPOSE 443/tcp 443/udp 444/udp  
  
RUN set -ex \  
&& apk add --no-cache --virtual /tmp/build-deps \  
autoconf \  
automake \  
g++ \  
gcc \  
git \  
libev-dev \  
libpcre32 \  
libtool \  
linux-headers \  
make \  
openssl \  
xmlto \  
zlib-dev \  
&& git clone --depth 1 --single-branch https://github.com/shadowsocks/simple-
obfs.git /tmp/simple-obfs \  
&& cd /tmp/simple-obfs \  
&& git submodule update --init --recursive \  
&& ./autogen.sh \  
&& ./configure \--disable-documentation \  
&& make install \  
&& git clone --depth 1 --single-branch https://github.com/pixers/runit-docker
/tmp/runit-docker \  
&& cd /tmp/runit-docker \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /tmp/simple-obfs /tmp/runit-docker \  
&& apk del /tmp/build-deps \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/local/bin/obfs-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache runit $runDeps \  
&& rm -rf /var/cache/apk/* \  
&& echo "#!/bin/sh" > /usr/bin/show \  
&& echo "/entry -mode show" >> /usr/bin/show \  
&& chmod +x /usr/bin/show  
  
COPY \--from=0 /entry /entry  
COPY \--from=xtaci/kcptun:latest /bin/server /usr/bin/kcp-server  
COPY runit/shadowsocks/run /etc/service/shadowsocks/run  
COPY runit/kcptun/run /etc/service/kcptun/run  

