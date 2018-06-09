FROM debian:7.8  
MAINTAINER Taotao Hsu <taotaohsu@gmail.com>  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
build-essential \  
automake && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

