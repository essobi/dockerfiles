FROM ajoergensen/baseimage-alpine  
MAINTAINER ajoergensen  
  
ARG PUREFTPD_VERSION=1.0.46  
  
RUN \  
apk -U update && \  
apk add \--virtual .builddeps libressl-dev build-base && \  
cd /tmp && \  
wget -q http://download.pureftpd.org/pub/pure-ftpd/releases/pure-
ftpd-$PUREFTPD_VERSION.tar.gz && \  
tar zxf pure-ftpd-$PUREFTPD_VERSION.tar.gz && \  
cd pure-ftpd-$PUREFTPD_VERSION && \  
./configure \--prefix=/usr \--without-humor \--without-capabilities
\--without-inetd \--with-throttling \--with-puredb \--with-tls \--with-altlog
&& \  
make -j$(getconf _NPROCESSORS_ONLN) && make install-strip && \  
cd / && \  
deps=$(scanelf --needed --nobanner /usr/sbin/pure-ftpd | awk '{ gsub(/,/,
"\nso:", $2); print "so:" $2 }' \  
| sort -u | xargs -r apk info \--installed | sort -u ) && \  
apk add \--virtual .rundeps $deps && \  
apk del .builddeps && \  
rm -rf /var/cache/apk/* /tmp/*  
  
ADD root/ /  
  
RUN \  
chmod -v +x /etc/cont-init.d/*.sh /etc/services.d/*/run  
# couple available volumes you may want to use  
VOLUME ["/home/ftpusers", "/etc/pure-ftpd/passwd"]  
  
EXPOSE 21 30000-30009  
  

