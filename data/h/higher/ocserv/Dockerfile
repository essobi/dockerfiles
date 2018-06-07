FROM alpine:3.4  
MAINTAINER Higher <cn.fly.higher@gmail.com>  
  
ENV OC_VERSION=0.11.8  
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
&& apk add --update nano gnutls gnutls-utils iptables libev libintl libnl3
libseccomp linux-pam lz4 openssl readline sed \  
&& apk add $buildDeps \  
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
&& cd / \  
&& rm -fr /usr/src/ocserv \  
&& apk del $buildDeps \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /etc/ocserv  
# Setup config  
COPY config /etc/ocserv  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 443  
CMD ["ocserv", "-c", "/etc/ocserv/ocserv.conf", "-f"]  

