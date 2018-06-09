FROM alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apk add \--update musl expat libressl libevent \  
build-base linux-headers musl-dev expat-dev libressl-dev libevent-dev && \  
set -x && \  
cd /root && \  
wget -qO- http://unbound.net/downloads/unbound-latest.tar.gz | tar xz && \  
cd ./unbound-*/ && \  
./configure \--prefix=/usr \--sysconfdir=/etc \--mandir=/usr/share/man
\--localstatedir=/var \--with-run-dir="" \--with-
pidfile=/var/run/unbound/unbound.pid \--with-libevent \--with-pthreads
\--with-ssl \--enable-subnet && \  
make && \  
make install && \  
cd /root && \  
rm -rf ./unbound-*/ && \  
apk del build-base linux-headers musl-dev expat-dev libressl-dev libevent-dev
&& \  
rm -rf /var/cache/apk/* && \  
chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["-c", "/etc/unbound/unbound.conf"]

