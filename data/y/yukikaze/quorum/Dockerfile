FROM ubuntu:16.04  
MAINTAINER Ashfaq Ahmed Shaik <https://github.com/0yukikaze0>  
  
# Set Proxy Variables if any  
ARG PROXY  
ENV http_proxy $PROXY  
ENV https_proxy $PROXY  
  
# Misc Environment Variables  
ENV PATH $PATH:/usr/local/go/bin  
  
# Install Pre Requisites  
RUN GO_RELEASE=go1.7.3.linux-amd64.tar.gz && \  
apt-get update && \  
apt-get install -y wget software-properties-common git build-essential && \  
add-apt-repository -y ppa:ethereum/ethereum && \  
  
# Install Go  
wget -q https://storage.googleapis.com/golang/${GO_RELEASE} && \  
tar -xvzf ${GO_RELEASE} && \  
mv go /usr/local/go && \  
rm -rf ${GO_RELEASE} && \  
  
# Clone Quorum and build binaries  
# => Building from master  
git clone https://github.com/jpmorganchase/quorum.git && \  
cd quorum && \  
make all && \  
# => Copy geth & bootnode binaries & Delete repo  
cp /quorum/build/bin/geth /usr/local/bin && \  
cp /quorum/build/bin/bootnode /usr/local/bin && \  
cd / && rm -rf /quorum && \  
  
# Install Constellation  
# Download version 0.1.0  
wget
https://github.com/jpmorganchase/constellation/releases/download/v0.1.0/constellation-0.1.0-ubuntu1604.tar.xz
&& \  
tar -xJf constellation-0.1.0-ubuntu1604.tar.xz && \  
mv ./constellation-0.1.0-ubuntu1604/* /usr/local/bin && \  
cd / && rm -rf /constellation-0.1.0-ubuntu1604 && rm -rf
./constellation-0.1.0-ubuntu1604.tar.xz && \  
  
# Clean up  
apt-get remove --purge -y wget software-properties-common build-essential git
$(apt-mark showauto) && \  
  
# Install SOLC  
apt-get update && \  
# Install SOLC and other dependencies for constellation  
apt-get install -y libdb-dev libsodium-dev zlib1g-dev libtinfo-dev libgmp-dev
solc && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/local/go  

