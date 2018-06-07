# build for amd64  
FROM alpine:latest  
# build for arm32 like [raspberry pi] or [tinker board]  
#FROM arm32v6/alpine:latest  
# for chinese user  
#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g'
/etc/apk/repositories  
  
RUN apk update && apk add \--no-cache build-base git autoconf automake gettext
pcre-dev libtool asciidoc xmlto udns-dev c-ares-dev libev-dev libsodium-dev
mbedtls-dev linux-headers && \  
git clone https://github.com/shadowsocks/shadowsocks-libev /tmp/shadowsocks-
libev && \  
cd /tmp/shadowsocks-libev && git submodule update \--init \--recursive && \  
./autogen.sh && ./configure && make && make install && \  
git clone https://github.com/shadowsocks/simple-obfs.git /tmp/simple-obfs && \  
cd /tmp/simple-obfs && git submodule update \--init \--recursive && \  
./autogen.sh && ./configure && make && make install && \  
apk del build-base git autoconf automake gettext libtool asciidoc xmlto linux-
headers && \  
rm -rf /tmp/shadowsocks-libev && rm -rf /tmp/simple-obfs  

