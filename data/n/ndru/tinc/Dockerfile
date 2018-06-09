FROM alpine  
MAINTAINER Andrew Tynefield <atynefield@gmail.com>  
  
ARG tincversion=1.0.30  
RUN apk add --no-cache readline-dev zlib-dev lzo-dev openssl-dev linux-headers
gcc g++ make ncurses-dev libpcap-dev readline zlib lzo libpcap && \  
wget http://www.tinc-vpn.org/packages/tinc-${tincversion}.tar.gz && \  
tar xzvf tinc-${tincversion}.tar.gz && \  
cd tinc-${tincversion} && \  
./configure --prefix=/usr --enable-jumbograms --enable-tunemu
--sysconfdir=/etc --localstatedir=/var && \  
make && make install src && \  
cd ../ && \  
rm -rfv tinc-${tincversion} && apk del --no-cache --purge readline-dev zlib-
dev lzo-dev openssl-dev linux-headers gcc g++ make ncurses-dev libpcap-dev
libc-utils  
  
EXPOSE 655/tcp 655/udp  
VOLUME /etc/tinc  

