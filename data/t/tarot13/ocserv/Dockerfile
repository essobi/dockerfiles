FROM alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
ARG OC_VERSION=0.12.0  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apk add --update nano iptables \  
musl openssl gnutls readline libnl3 lz4 lz4-libs libseccomp libev geoip \  
build-base xz linux-headers musl-dev gnutls-dev readline-dev libnl3-dev
lz4-dev libseccomp-dev libev-dev geoip-dev && \  
set -x && \  
cd /root && \  
OC_FILE="ocserv-$OC_VERSION" && \  
wget ftp://ftp.infradead.org/pub/ocserv/$OC_FILE.tar.xz && \  
tar xJf $OC_FILE.tar.xz && \  
rm $OC_FILE.tar.xz && \  
cd $OC_FILE && \  
./configure && \  
make -j"$(nproc)" && \  
make install && \  
cd /root && \  
rm -rf $OC_FILE && \  
apk del build-base xz linux-headers musl-dev gnutls-dev readline-dev
libnl3-dev lz4-dev libseccomp-dev libev-dev geoip-dev && \  
rm -rf /var/cache/apk/* && \  
mkdir /var/lib/ocserv && \  
chmod +x /entrypoint.sh  
  
ENV TERM xterm  
  
EXPOSE 443/tcp 443/udp  
  
ENTRYPOINT ["/entrypoint.sh"]

