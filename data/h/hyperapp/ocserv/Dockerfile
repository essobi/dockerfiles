FROM alpine:edge  
MAINTAINER hyperapp  
  
RUN apk add --update --no-cache musl-dev iptables libev openssl gnutls-dev
readline-dev libnl3-dev lz4-dev libseccomp-dev gnutls-utils  
  
ARG OC_VERSION=0.11.8  
ENV PORT=443  
ENV VPN_NETWORK=10.24.0.0  
ENV VPN_NETMASK=255.255.255.0  
ENV LAN_NETWORK=192.168.0.0  
ENV LAN_NETMASK=255.255.0.0  
ENV VPN_USERNAME=hyperapp  
ENV VPN_PASSWORD=hyperapp  
ENV TERM=xterm  
  
RUN buildDeps="xz gcc autoconf make linux-headers libev-dev "; \  
set -x \  
&& apk add --no-cache $buildDeps \  
&& mkdir /src && cd /src \  
&& OC_FILE="ocserv-$OC_VERSION" \  
&& rm -fr download.html \  
&& wget ftp://ftp.infradead.org/pub/ocserv/$OC_FILE.tar.xz \  
&& tar xJf $OC_FILE.tar.xz \  
&& rm -fr $OC_FILE.tar.xz \  
&& cd $OC_FILE \  
&& sed -i '/#define DEFAULT_CONFIG_ENTRIES /{s/96/200/}' src/vpn.h \  
&& ./configure \  
&& make -j"$(nproc)" \  
&& make install \  
&& mkdir -p /etc/ocserv \  
&& cp ./doc/sample.config /etc/ocserv/ocserv.conf \  
&& cd \  
&& rm -fr ./$OC_FILE \  
&& apk del --purge $buildDeps \  
&& rm -rf /src  
  
RUN set -x \  
&& sed -i 's/\\.\/sample\\.passwd/\/etc\/ocserv\/ocpasswd/'
/etc/ocserv/ocserv.conf \  
&& sed -i 's/\\(max-same-clients = \\)2/\110/' /etc/ocserv/ocserv.conf \  
&& sed -i 's/\\.\\.\/tests/\/etc\/ocserv/' /etc/ocserv/ocserv.conf \  
&& sed -i 's/#\\(compression.*\\)/\1/' /etc/ocserv/ocserv.conf \  
&& sed -i '/^ipv4-network = /{s/192.168.1.0/192.168.99.0/}'
/etc/ocserv/ocserv.conf \  
&& sed -i 's/192.168.1.2/8.8.8.8/' /etc/ocserv/ocserv.conf \  
&& sed -i 's/^route/#route/' /etc/ocserv/ocserv.conf \  
&& sed -i 's/^no-route/#no-route/' /etc/ocserv/ocserv.conf  
  
COPY cn-no-route.txt /etc/ocserv  
COPY ocserv.conf /etc/ocserv  
WORKDIR /etc/ocserv  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY init.sh /init.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE $PORT/tcp $PORT/udp  

