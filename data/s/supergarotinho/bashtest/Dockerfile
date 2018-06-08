##  
FROM ubuntu:12.04  
MAINTAINER Anderson Santos anderson@gruponeuro.com.br  
  
RUN apt-get update && \  
apt-get install -y \  
binutils-dev \  
build-essential \  
cmake \  
git \  
libcurl4-openssl-dev \  
#libiberty-dev \ - está no binutls-dev no 12.04  
libdw-dev \  
pkg-config \  
python \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /root && \  
git clone https://github.com/SimonKagstrom/kcov && \  
cd kcov && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr . && \  
make && \  
make install \  
&& cd / \  
&& rm -rf /root/kcov  
  
RUN cd /root && \  
git clone https://github.com/kward/shunit2  
  
VOLUME /source  
WORKDIR /source  

