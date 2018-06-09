#  
# Dockerfile for ocserv  
#  
FROM alpine  
  
MAINTAINER stawidy <duyizhaozj321@yahoo.com>  
  
ARG OC_VERSION=0.12.1  
RUN buildDeps=" \  
curl \  
g++ \  
gnutls-dev \  
gpgme \  
libev-dev \  
libnl3-dev \  
libseccomp-dev \  
linux-headers \  
linux-pam-dev \  
lz4-dev \  
make \  
readline-dev \  
tar \  
xz \  
"; \  
set -x \  
&& apk add --update --virtual .build-deps $buildDeps \  
&& curl -SL "ftp://ftp.infradead.org/pub/ocserv/ocserv-$OC_VERSION.tar.xz" -o
ocserv.tar.xz \  
&& curl -SL "ftp://ftp.infradead.org/pub/ocserv/ocserv-$OC_VERSION.tar.xz.sig"
-o ocserv.tar.xz.sig \  
&& gpg --keyserver pool.sks-keyservers.net --recv-key 7F343FA7 \  
&& gpg --keyserver pool.sks-keyservers.net --recv-key 96865171 \  
&& gpg --verify ocserv.tar.xz.sig \  
&& mkdir -p /usr/src/ocserv \  
&& tar -xf ocserv.tar.xz -C /usr/src/ocserv --strip-components=1 \  
&& rm ocserv.tar.xz* \  
&& cd /usr/src/ocserv \  
&& ./configure \  
&& make \  
&& make install \  
&& mkdir -p /etc/ocserv \  
&& cd / \  
&& rm -fr /usr/src/ocserv \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/local/sbin/ocserv \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .run-deps $runDeps gnutls-utils iptables \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
ENV CA_CN="Sample CN" \  
CA_ORG="Sample ORG" \  
CA_DAYS=9999 \  
SRV_CN="your.domain.name" \  
SRV_ORG="Sample ORG" \  
SRV_DAYS=9999 \  
VPN_NETWORK=10.0.6.0 \  
VPN_NETMASK=255.255.255.0  
WORKDIR /etc/ocserv  
  
COPY ocserv.conf /etc/ocserv/ocserv.conf  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 443/tcp 443/udp  
CMD ["ocserv", "-c", "/etc/ocserv/ocserv.conf", "-f"]  

