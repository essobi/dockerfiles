FROM alpine:3.6  
  
MAINTAINER Tommy Lau <tommy@gen-new.com>  
  
ENV OC_VERSION=0.11.8  
ENV AUTOGEN_VERSION=5.18.12  
  
COPY ocadduser /usr/bin/ocadduser  
  
  
  
RUN buildDeps=" \  
autoconf \  
automake \  
abi-compliance-checker \  
file \  
guile-dev \  
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
&& apk add --update libtool gnutls gnutls-utils iptables libev libintl libnl3
libseccomp linux-pam lz4-libs openssl readline sed \  
&& apk add --update --virtual .build-deps $buildDeps \  
&& cd ~ \  
&& RADCLI_VERSION=`curl -s "https://github.com/radcli/radcli/releases/latest"
| sed -n 's/^.*tag\/\(.*\)".*/\1/p'` \  
&& curl -SL "https://github.com/radcli/radcli/archive/$RADCLI_VERSION.tar.gz"
-o radcli.tar.gz \  
&& mkdir -p /usr/src/radcli \  
&& tar -xf radcli.tar.gz -C /usr/src/radcli --strip-components=1 \  
&& rm radcli.tar.gz \  
&& cd /usr/src/radcli \  
&& chmod +x autogen.sh \  
&& ./autogen.sh \  
&& ./configure --sysconfdir=/etc --prefix=/usr \  
&& make \  
&& make install \  
&& cd ~ \  
&& rm -fr /usr/src/radcli \  
&& curl -SL
"http://ftp.gnu.org/gnu/autogen/rel$AUTOGEN_VERSION/autogen-$AUTOGEN_VERSION.tar.xz"
-o autogen.tar.xz \  
&& mkdir -p /usr/src/autogen \  
&& tar -xf autogen.tar.xz -C /usr/src/autogen --strip-components=1 \  
&& rm autogen.tar.xz \  
&& cd /usr/src/autogen \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install \  
&& cd ~ \  
&& rm -fr /usr/src/autogen \  
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
&& cp /usr/src/ocserv/doc/sample.config /etc/ocserv/ocserv.conf \  
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
COPY groupinfo.txt /tmp/  
RUN set -x \  
&& sed -i 's/\.\/sample\.passwd/\/etc\/ocserv\/ocpasswd/'
/etc/ocserv/ocserv.conf \  
&& sed -i 's/\(max-same-clients = \)2/\110/' /etc/ocserv/ocserv.conf \  
&& sed -i 's/\.\.\/tests/\/etc\/ocserv/' /etc/ocserv/ocserv.conf \  
&& sed -i 's/#\(compression.*\)/\1/' /etc/ocserv/ocserv.conf \  
&& sed -i '/^ipv4-network = /{s/192.168.1.0/192.168.99.0/}'
/etc/ocserv/ocserv.conf \  
&& sed -i 's/192.168.1.2/8.8.8.8/' /etc/ocserv/ocserv.conf \  
&& sed -i 's/^route/#route/' /etc/ocserv/ocserv.conf \  
&& sed -i 's/^no-route/#no-route/' /etc/ocserv/ocserv.conf \  
&& mkdir -p /etc/ocserv/config-per-group \  
&& cat /tmp/groupinfo.txt >> /etc/ocserv/ocserv.conf \  
&& rm -fr /tmp/cn-no-route.txt \  
&& rm -fr /tmp/groupinfo.txt  
  
WORKDIR /etc/ocserv  
  
COPY All /etc/ocserv/config-per-group/All  
COPY cn-no-route.txt /etc/ocserv/config-per-group/Route  
  
COPY docker-entrypoint.sh /entrypoint.sh  
VOLUME ["/etc/ocserv", "/etc/radiusclient"]  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 443  
CMD ["ocserv", "-c", "/etc/ocserv/ocserv.conf", "-f"]

