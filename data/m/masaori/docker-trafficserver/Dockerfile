FROM buildpack-deps:wily  
  
ENV ATS_VERSION 6.0.0  
WORKDIR /opt  
  
RUN apt-get update  
  
RUN wget
"http://archive.apache.org/dist/trafficserver/trafficserver-${ATS_VERSION}.tar.bz2"
&& \  
wget
"http://archive.apache.org/dist/trafficserver/trafficserver-${ATS_VERSION}.tar.bz2.asc"
&& \  
wget "http://archive.apache.org/dist/trafficserver/KEYS"  
  
RUN gpg --import KEYS && \  
gpg --verify trafficserver-${ATS_VERSION}.tar.bz2.asc  
  
RUN apt-get install -y \  
openssl \  
tcl-dev \  
expat \  
libpcre3-dev \  
libcap-dev\  
hwloc \  
libncurses5-dev  
  
RUN tar xvf trafficserver-${ATS_VERSION}.tar.bz2 && \  
cd trafficserver-${ATS_VERSION} && \  
autoreconf -if && \  
./configure && \  
make -j$(nproc) && \  
make install  

