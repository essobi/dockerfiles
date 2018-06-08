FROM ubuntu:trusty  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
WORKDIR /etc/ocserv  
  
# Prepare building environment  
RUN apt-get update && apt-get install build-essential libwrap0-dev
libpam0g-dev libdbus-1-dev libreadline-dev libnl-route-3-dev libpcl1-dev
libopts25-dev autogen libgnutls28 libgnutls28-dev libseccomp-dev iptables wget
gnutls-bin libprotobuf-c0-dev protobuf-c-compiler libprotobuf-dev protobuf-
compiler libprotoc-dev libtalloc-dev libhttp-parser-dev -y  
  
# Use version 0.10.11  
RUN export ocserv_version=0.10.11 \  
&& wget ftp://ftp.infradead.org/pub/ocserv/ocserv-$ocserv_version.tar.xz &&
tar xvf ocserv-$ocserv_version.tar.xz \  
&& cd ocserv-$ocserv_version && sed -i 's/define DEFAULT_CONFIG_ENTRIES
96/define DEFAULT_CONFIG_ENTRIES 200/g' src/vpn.h \  
&& ./configure --prefix=/usr --sysconfdir=/etc --with-local-talloc && make &&
make install \  
&& rm -rf /root/download.html && rm -rf ocserv-*  
  
# Before starting this daemon, make sure you have certificates generated
correctly.  
## Please check the user document for more information.  
CMD ["vpn_run"]

