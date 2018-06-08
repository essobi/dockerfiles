FROM alpine:3.6  
  
MAINTAINER Thomas Leister <thomas.leister@mailbox.org>  
  
RUN apk upgrade --update && \  
apk add --no-cache --virtual /tmp/.build-deps \  
libressl \  
libressl-dev \  
zlib \  
zlib-dev \  
git \  
gcc \  
make \  
linux-headers \  
musl-dev \  
musl-utils \  
build-base \  
abuild \  
binutils \  
bash && \  
rm -rfv /var/cache/apk/* && \  
git clone https://github.com/peervpn/peervpn.git /tmp/peervpn.git && \  
cd /tmp/peervpn.git && \  
CFLAGS=-Wall make -j$(getconf _NPROCESSORS_ONLN) && \  
cp peervpn /sbin/peervpn && \  
install -m 755 peervpn /sbin/peervpn && \  
cd / && \  
rm -rf /tmp/peervpn.git && \  
apk del /tmp/.build-deps  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

