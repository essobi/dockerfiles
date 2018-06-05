FROM ubuntu:latest  
  
MAINTAINER Min Kim <minskim@pkgsrc.org>  
  
RUN adduser --disabled-login pbulk  
  
RUN \  
apt-get update && \  
apt-get install -y \  
g++ \  
git  
  
RUN \  
cd /usr && \  
git clone -b trunk \  
\--depth 1 https://github.com/NetBSD/pkgsrc.git && \  
cd /usr/pkgsrc/mk/pbulk && env SH=/bin/bash sh ./pbulk.sh -n && \  
cd / && rm -rf /usr/pkgsrc  

