## build script based on format of official haproxy dockerfile  
## https://github.com/docker-library/haproxy/blob/master/1.8/alpine/Dockerfile  
  
FROM alpine:edge  
  
ENV VERSION 1.3.0  
  
RUN set -x \  
\  
&& apk add --no-cache --virtual .build-deps \  
g++ \  
make \  
libressl \  
boost-dev \  
lua5.3-dev \  
libedit-dev \  
libsodium-dev \  
protobuf-dev \  
re2-dev \  
\  
&& mkdir -p /usr/src \  
\  
## build  
&& cd / \  
&& wget -O dnsdist.tar.bz2
https://downloads.powerdns.com/releases/dnsdist-$VERSION.tar.bz2 \  
&& tar xf dnsdist.tar.bz2 --strip-components=1 -C /usr/src \  
&& rm dnsdist.tar.bz2 \  
&& cd /usr/src \  
\  
&& CFLAGS='-Os' CXXFLAGS='-Os' ./configure \  
\--prefix=/usr/local \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--enable-libsodium \  
\--enable-dnscrypt \  
\--enable-re2 \  
\--disable-static \  
&& make -j "$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
\  
## cleanup  
&& cd / \  
&& rm -rf /usr/src \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --virtual .rundeps $runDeps \  
&& apk del .build-deps \  
\  
## user  
&& adduser -DH _dnsdist  
  
ENTRYPOINT ["dnsdist", "--supervised", "--disable-syslog", "-u", "_dnsdist",
"-g", "_dnsdist"]  

