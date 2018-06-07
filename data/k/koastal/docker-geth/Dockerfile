FROM ubuntu:xenial  
MAINTAINER zhezhao zhezhao1993@qq.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
&& \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install software-properties-common && \  
add-apt-repository -y ppa:ethereum/ethereum && \  
apt-get update && \  
apt-get -y install ethereum && \  
apt-get -y install net-tools && \  
apt-get -y install telnet && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/local/blockchain  
  
WORKDIR /var/local/blockchain  
  
EXPOSE 8545 30303

