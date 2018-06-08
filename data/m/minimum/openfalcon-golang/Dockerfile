FROM ubuntu:14.04  
MAINTAINER minimum@cepave.com  
  
ENV GOLANG_VERSION=1.6 GOLANG_OS=linux GOLANG_ARCH=amd64  
ENV GOROOT=/home/go GOPATH=/home/workspace  
ENV PATH=$GOROOT/bin:$GOPATH/bin:$PATH  
  
WORKDIR /home  
  
RUN \  
apt-get update && \  
apt-get install -y wget vim git && \  
wget
https://storage.googleapis.com/golang/go$GOLANG_VERSION.$GOLANG_OS-$GOLANG_ARCH.tar.gz
&& \  
tar -xzf go$GOLANG_VERSION.$GOLANG_OS-$GOLANG_ARCH.tar.gz && \  
mkdir -p workspace/src && \  
apt-get remove -y wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
go$GOLANG_VERSION.$GOLANG_OS-$GOLANG_ARCH.tar.gz  
  

