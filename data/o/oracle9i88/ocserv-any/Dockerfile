FROM alpine:edge  
MAINTAINER bao3.cn@gmail.com  
  
RUN apk add --update --no-cache musl-dev iptables libev openssl gnutls-dev
readline-dev libnl3-dev lz4-dev libseccomp-dev gnutls-utils  
  
ARG OC_VERSION=0.11.9  
ENV PORT=443  
ENV VPN_DOMAIN=example.com  
ENV VPN_NETWORK=10.24.0.0  
ENV VPN_NETMASK=255.255.255.0  
ENV LAN_NETWORK=192.168.0.0  
ENV LAN_NETMASK=255.255.0.0  
ENV VPN_USERNAME=hyperapp  
ENV VPN_PASSWORD=hyperapp  
#OC_CERT_AND_PLAIN 是代表您是否需要同时具备密码验证和证书验证功能  
#由于 anyconnect 的特性，如果使用密码验证，客户端软件在每次连接都必须输入一次，不能保存和记忆。所以建议禁用掉就好了  
# true 代表两各方式都有，false 代表禁用  
ENV OC_CERT_AND_PLAIN=false  
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
  
#COPY new_CN_route.txt /etc/ocserv/cn-no-route.txt  
COPY new_CN_route.txt /etc/ocserv/config-per-user/route.txt  
COPY ocserv.conf /etc/ocserv  
WORKDIR /etc/ocserv  
VOLUME ["/etc/ocserv/certs/"]  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY init.sh /init.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE $PORT/tcp $PORT/udp  

