FROM debian:jessie  
MAINTAINER Alexandre Léveillé <leveille.alexandre+atsdocker@gmail.com>  
  
ENV PREFIX="/opt/ts"  
ENV PATH="${PREFIX}/bin:${PATH}"  
ENV TS_VERSION=6.2.1  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
gcc \  
libc6-dev \  
pkgconf \  
libssl-dev \  
tcl \  
tcl-dev \  
libxml2-dev \  
libpcre3-dev \  
hwloc \  
lua5.2 \  
net-tools \  
dnsutils \  
netcat \  
tcpdump \  
wget \  
curl \  
openssl \  
ssl-cert \  
ca-certificates \  
bzip2 && \  
rm -rf /var/lib/apt/lists/* && \  
cd /opt && \  
wget
http://mirror.csclub.uwaterloo.ca/apache/trafficserver/trafficserver-${TS_VERSION}.tar.bz2
&& \  
tar -xf trafficserver-${TS_VERSION}.tar.bz2 && \  
cd trafficserver-${TS_VERSION} && \  
./configure --prefix=${PREFIX} && \  
make && \  
make install  
  
EXPOSE 80 443 8080  
  
CMD ["sh", "-c", "${PREFIX}/bin/traffic_cop"]  

