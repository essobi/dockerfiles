#  
# libsodium Dockerfile  
#  
# https://github.com/lukin0110/docker-libsodium  
#  
# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Maarten Huijsmans <maarten.huijsmans@gmail.com>  
  
# Define workdir  
WORKDIR /root  
  
# Install some tools: gcc build tools, unzip, etc  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install curl build-essential unzip  
  
# Download and install libsodium  
# https://download.libsodium.org/doc/  
# Download & extract & make libsodium  
# Move libsodium build  
RUN \  
mkdir -p /tmpbuild/libsodium && \  
cd /tmpbuild/libsodium && \  
curl -L
https://download.libsodium.org/libsodium/releases/libsodium-1.0.3.tar.gz -o
libsodium-1.0.3.tar.gz && \  
tar xfvz libsodium-1.0.3.tar.gz && \  
cd /tmpbuild/libsodium/libsodium-1.0.3/ && \  
./configure && \  
make && make check && \  
make install && \  
mv src/libsodium /usr/local/ && \  
rm -Rf /tmpbuild/  
  
# Define default command  
CMD ["bash"]  

