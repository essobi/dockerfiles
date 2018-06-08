FROM ubuntu:16.04  
MAINTAINER Dennis Parchkov  
  
USER root  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
apache2 \  
wget \  
iperf \  
tcpdump \  
net-tools \  
iproute \  
iputils-ping \  
vim \  
iptables \  
build-essential checkinstall \  
libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev
libgdbm-dev libc6-dev libbz2-dev  
RUN apt-get install -y python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
  

