FROM ubuntu:xenial  
MAINTAINER zhezhao zhezhao1993@qq.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV IPFS_VERSION v0.4.13  
ENV URL https://dist.ipfs.io/go-ipfs/${IPFS_VERSION}/go-
ipfs_${IPFS_VERSION}_linux-amd64.tar.gz  
ENV IPFS_PATH /var/local/go-ipfs  
  
WORKDIR /var/local  
  
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
&& \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install net-tools && \  
apt-get -y install telnet && \  
apt-get -y install wget && \  
wget ${URL} -O go-ipfs.tar.gz && \  
tar xzf go-ipfs.tar.gz && \  
rm go-ipfs.tar.gz && \  
mv go-ipfs/ipfs /usr/local/bin/ipfs && \  
rm go-ipfs/* && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ipfs-swarm-key-gen ipfs-swarm-key-gen  
RUN chmod u+x ipfs-swarm-key-gen  
  
EXPOSE 5001 8080

