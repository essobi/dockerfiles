FROM alpine:latest AS build-env  
  
ENV
LIBRESSL_SHA="5fafff32bc4effa98c00278206f0aeca92652c6a8101b2c5da3904a5a3deead2d1e3ce979c644b8dc6060ec216eb878a5069324a0396c0b1d7b6f8169d509e9b"
\  
LIBRESSL_DOWNLOAD_URL="https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.7.3.tar.gz"  
RUN BUILD_DEPS='build-base automake autoconf libtool ca-certificates curl file
linux-headers' && \  
set -x && \  
apk add --no-cache \  
$BUILD_DEPS && \  
mkdir -p /tmp/src/libressl && \  
cd /tmp/src && \  
curl -sSL $LIBRESSL_DOWNLOAD_URL -o libressl.tar.gz && \  
echo "${LIBRESSL_SHA} *libressl.tar.gz" | sha512sum -c - && \  
cd libressl && \  
tar xzf ../libressl.tar.gz --strip-components=1 && \  
rm -f ../libressl.tar.gz && \  
autoreconf -vif && \  
./configure --prefix=/opt/libressl && \  
make check && make install  
  
ENV
UNBOUND_SHA="99a68abf1f60f6ea80cf2973906df44da9c577d8cac969824af1ce9ca385a2e84dd684937480da87cb73c7dc41ad5c00b0013ec74103eadb8fd7dc6f98a89255"
\  
UNBOUND_DOWNLOAD_URL="https://www.unbound.net/downloads/unbound-1.7.1.tar.gz"  
RUN BUILD_DEPS='build-base curl file linux-headers' && \  
set -x && \  
apk add --no-cache \  
$BUILD_DEPS \  
libevent \  
libevent-dev \  
expat \  
expat-dev && \  
mkdir -p /tmp/src/unbound && \  
cd /tmp/src && \  
curl -sSL $UNBOUND_DOWNLOAD_URL -o unbound.tar.gz && \  
echo "${UNBOUND_SHA} *unbound.tar.gz" | sha512sum -c - && \  
cd unbound && \  
tar xzf ../unbound.tar.gz --strip-components=1 && \  
rm -f ../unbound.tar.gz && \  
addgroup -S unbound 2>/dev/null && \  
adduser -S -D -H -h /etc/unbound -s /sbin/nologin -G unbound -g "Unbound user"
unbound 2>/dev/null && \  
AR='gcc-ar' RANLIB='gcc-ranlib' autoreconf -vif && \  
./configure AR='gcc-ar' RANLIB='gcc-ranlib' \--prefix=/opt/unbound --with-
pthreads \  
\--with-username=unbound \--with-ssl=/opt/libressl --with-libevent \  
\--enable-event-api && \  
make install && \  
curl -s ftp://FTP.INTERNIC.NET/domain/named.cache -o
/opt/unbound/etc/unbound/root.hints && \  
rm /opt/unbound/etc/unbound/unbound.conf  
RUN set -x && \  
rm -fr /opt/libressl/share && \  
rm -fr /opt/libressl/include/* && \  
rm /opt/libressl/lib/*.a /opt/libressl/lib/*.la && \  
rm -fr /opt/unbound/share /opt/unbound/include /opt/unbound/lib/*.a
/opt/unbound/lib/*.la && \  
find /opt/libressl/bin -type f | xargs strip --strip-all && \  
find /opt/libressl/lib/lib* -type f | xargs strip --strip-all && \  
find /opt/unbound/lib/lib* -type f | xargs strip --strip-all && \  
strip \--strip-all /opt/unbound/sbin/unbound && \  
strip \--strip-all /opt/unbound/sbin/unbound-anchor && \  
strip \--strip-all /opt/unbound/sbin/unbound-checkconf && \  
strip \--strip-all /opt/unbound/sbin/unbound-control && \  
strip \--strip-all /opt/unbound/sbin/unbound-host  
# ----------------------------------------------------------------------------  
FROM alpine:latest  
COPY \--from=build-env /opt/ /opt/  
RUN set -x && \  
apk add --no-cache \  
libevent \  
expat && \  
addgroup -g 59834 -S unbound 2>/dev/null && \  
adduser -S -D -H -u 59834 -h /etc/unbound -s /sbin/nologin -G unbound -g
"Unbound user" unbound 2>/dev/null && \  
mkdir -p /opt/unbound/etc/unbound/unbound.conf.d && \  
mkdir -p /var/log/unbound && chown unbound.unbound /var/log/unbound && \  
rm -rf /usr/share/docs/* /usr/share/man/* /var/log/*  
COPY resources/unbound.sh /  
RUN chmod +x /unbound.sh  
COPY resources/unbound.conf /opt/unbound/etc/unbound/  
COPY resources/allow.conf /opt/unbound/etc/unbound/unbound.conf.d/  
EXPOSE 53/udp  
CMD ["/unbound.sh"]  

