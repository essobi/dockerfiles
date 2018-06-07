FROM ubuntu:14.04  
MAINTAINER Brandon Murphy <github@zoomequipd.com>  
  
# Install depends  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
bison \  
flex \  
libssl-dev \  
netbase  
  
# Add source files  
ADD src /usr/local/src/  
  
# install specific version of major depends  
RUN cd /usr/local/src/ && tar zxf libdnet-1.12.tgz && cd libdnet-1.12 &&
./configure ; make ; make install  
RUN cd /usr/local/src/ && tar zxf libpcap-1.7.3.tar.gz && cd libpcap-1.7.3 &&
./configure ; make ; make install  
RUN cd /usr/local/src/ && tar zxf zlib-1.2.8.tar.gz && cd zlib-1.2.8 &&
./configure ; make ; make install  
RUN cd /usr/local/src/ && tar zxf pcre-8.37.tar.gz && cd pcre-8.37 &&
./configure --enable-jit --enable-pcregrep-libz --enable-pcre16 --enable-
pcre32 --enable-utf --enable-unicode-properties ; make ; make install  
  
#Compile DAQ  
RUN cd /usr/local/src/ && tar zxf daq-2.0.4.tar.gz && cd daq-2.0.4 &&
./configure --disable-ipfw-module --disable-nfq-module --disable-ipq-module ;
make ; make install  
  
# Compile Snort  
RUN cd /usr/local/src/ && tar zxf snort-2.9.7.2.tar.gz && cd snort-2.9.7.2 &&
./configure --enable-control-socket --enable-sourcefire --enable-large-pcap
--enable-zlib --enable-perfprofiling ; make ; make install  
  
RUN ldconfig  
RUN ln -s /usr/local/lib/libdnet.1.0.1 /usr/lib/libdnet.1  
RUN mkdir /var/log/snort  
  
RUN /usr/local/bin/snort -V  
  
# CLEAN UP - TODO  

