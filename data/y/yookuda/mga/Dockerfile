FROM ubuntu:14.04  
MAINTAINER yookuda <yookuda@nig.ac.jp>  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get clean  
WORKDIR /tmp  
RUN wget http://metagene.nig.ac.jp/metagene/mga_x86_64.tar.gz && \  
tar xzvf mga_x86_64.tar.gz && \  
cp mga_linux_ia64 /usr/local/bin/mga && \  
rm -rf /tmp/*  
RUN mkdir /data  

