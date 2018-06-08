FROM alpine  
MAINTAINER oldpussy  
  
ARG SS_VER=3.1.0  
ARG SS_URL=https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz  
ARG NGINX_VERSION=1.13.6  
ARG OBFS=www.ibm.com  
  
ENV SERVER_PORT 8388  
ENV PASSWD=  
ENV METHOD chacha20-ietf-poly1305  
  
RUN apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
gnupg \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
autoconf \  
build-base \  
curl \  
libev-dev \  
libtool \  
libsodium-dev \  
mbedtls-dev \  
tar \  
c-ares-dev \  
automake \  
asciidoc \  
xmlto \  
git &&\  
cd /tmp &&\  
curl -sSL $SS_URL | tar xz --strip 1 && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
CONFIG="\  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--with-http_ssl_module \  
\--pid-path=/var/run/nginx.pid" &&\  
curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz &&\  
mkdir -p /usr/src &&\  
tar -zxC /usr/src -f nginx.tar.gz &&\  
cd /usr/src/nginx-$NGINX_VERSION &&\  
./configure $CONFIG &&\  
make -j$(getconf _NPROCESSORS_ONLN) &&\  
make install &&\  
git clone https://github.com/shadowsocks/simple-obfs.git &&\  
cd simple-obfs &&\  
git submodule update --init --recursive &&\  
./autogen.sh &&\  
./configure && make &&\  
make install &&\  
rm -rf /usr/src/nginx-$NGINX_VERSION /tmp &&\  
runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so
/usr/local/bin/obfs-server /usr/bin/ss-* /tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" &&\  
apk add --no-cache --virtual .rundeps $runDeps &&\  
apk del .build-deps  
  
COPY ss-obfs.sh /usr/bin/ss-obfs.sh  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY $OBFS.crt /etc/nginx/$OBFS.crt  
COPY $OBFS.key /etc/nginx/$OBFS.key  
RUN chmod 755 /usr/bin/ss-obfs.sh  
  
EXPOSE $SERVER_PORT/tcp $SERVER_PORT/udp  
CMD ss-obfs.sh $SERVER_PORT $PASSWD $METHOD  

