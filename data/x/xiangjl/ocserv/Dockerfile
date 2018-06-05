FROM alpine:3.7  
  
MAINTAINER XiangJL <xjl-tommy@qq.com>  
  
ENV OC_VERSION=0.12.1  
  
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
&& mkdir -p /docker \  
&& cd /docker \  
&& apk add --update --virtual .build-deps $buildDeps \  
&& curl -SL "ftp://ftp.infradead.org/pub/ocserv/ocserv-$OC_VERSION.tar.xz" -o
ocserv.tar.xz \  
&& curl -SL "ftp://ftp.infradead.org/pub/ocserv/ocserv-$OC_VERSION.tar.xz.sig"
-o ocserv.tar.xz.sig \  
&& gpg --keyserver pgp.mit.edu --recv-key 7F343FA7 \  
&& gpg --keyserver pgp.mit.edu --recv-key 96865171 \  
&& gpg --verify ocserv.tar.xz.sig \  
&& mkdir -p /usr/src/ocserv \  
&& tar -xf ocserv.tar.xz -C /usr/src/ocserv --strip-components=1 \  
&& rm ocserv.tar.xz* \  
&& cd /usr/src/ocserv \  
&& ./configure \  
&& make \  
&& make install \  
&& mkdir -p /etc/ocserv \  
&& mkdir -p /docker/config \  
&& cp /usr/src/ocserv/doc/sample.config /docker/config/ocserv.conf \  
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
  
# Setup config  
COPY docker-ocertsmgr.sh /docker/ocertsmgr.sh  
COPY groupinfo.txt /tmp/  
RUN set -x \  
&& sed -i 's/\.\/sample\.passwd/\/etc\/ocserv\/ocpasswd/'
/docker/config/ocserv.conf \  
&& sed -i 's/\(max-same-clients = \)2/\110/' /docker/config/ocserv.conf \  
&& sed -i 's/\.\.\/tests/\/etc\/ocserv/' /docker/config/ocserv.conf \  
&& sed -i 's/#\(compression.*\)/\1/' /docker/config/ocserv.conf \  
&& sed -i 's/^#enable-auth = "certificate"/enable-auth = "certificate"/'
/docker/config/ocserv.conf \  
&& sed -i 's/^cert-user-oid = 0.9.2342.19200300.100.1.1/cert-user-oid =
2.5.4.3/' /docker/config/ocserv.conf \  
&& sed -i 's/#cert-group-oid/cert-group-oid/' /docker/config/ocserv.conf \  
&& sed -i 's/^#crl = \/path\/to\/crl.pem/crl = \/etc\/ocserv\/certs\/crl.pem/'
/docker/config/ocserv.conf \  
&& sed -i '/^ipv4-network = /{s/192.168.1.0/192.168.99.0/}'
/docker/config/ocserv.conf \  
&& sed -i 's/192.168.1.2/8.8.8.8/' /docker/config/ocserv.conf \  
&& sed -i 's/^route/#route/' /docker/config/ocserv.conf \  
&& sed -i 's/^no-route/#no-route/' /docker/config/ocserv.conf \  
&& ln -sf /docker/ocertsmgr.sh /usr/local/bin/ocertsmgr \  
&& mkdir -p /docker/config/config-per-group \  
&& cat /tmp/groupinfo.txt >> /docker/config/ocserv.conf \  
&& rm -fr /tmp/groupinfo.txt  
  
WORKDIR /etc/ocserv  
  
COPY all-route.txt /docker/config/config-per-group/All  
COPY cn-no-route.txt /docker/config/config-per-group/Route  
  
COPY docker-entrypoint.sh /docker/startup.sh  
ENTRYPOINT ["/docker/startup.sh"]  
  
EXPOSE 443  
CMD ["ocserv", "-c", "/etc/ocserv/ocserv.conf","-f"]  

