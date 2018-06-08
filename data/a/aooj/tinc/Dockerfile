FROM alpine:latest  
MAINTAINER AooJ <aooj@n13.cz>  
  
# http://www.tinc-vpn.org/pipermail/tinc/2016-May/004572.html  
# As it turns out, it's a bug in the igmp snooping code in the kernel that's
the problem with multicast traffic not being forwarded.  
# echo 0 > /sys/devices/virtual/net/br0/bridge/multicast_snooping  
ENV DEV_PACKAGES="build-base make zlib-dev lzo-dev libressl-dev linux-headers
ncurses-dev readline-dev"  
ENV TINC_VERSION=1.1pre15  
  
RUN apk add --update ncurses readline lzo zlib $DEV_PACKAGES && \  
cd /tmp && \  
wget http://www.tinc-vpn.org/packages/tinc-${TINC_VERSION}.tar.gz && \  
tar -xzf tinc-${TINC_VERSION}.tar.gz && \  
cd tinc-${TINC_VERSION} && \  
./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--mandir=/usr/share/man \  
\--infodir=/usr/share/info \  
\--localstatedir=/var \  
\--enable-jumbograms \  
\--enable-lzo \  
\--enable-zlib && \  
make && \  
make install && \  
apk del $DEV_PACKAGES && \  
rm -rf /var/cache/apk/* && \  
tinc --version  
  
EXPOSE 655/tcp 655/udp  
VOLUME /etc/tinc  
  
ENTRYPOINT [ "/usr/sbin/tinc" ]  
CMD [ "start", "-D", "-U", "nobody" ]  

