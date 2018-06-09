FROM debian:7.8  
MAINTAINER Taotao Hsu <taotaohsu@gmail.com>  
  
RUN apt-get update && \  
apt-get upgrade -y --force-yes && \  
apt-get install -y --force-yes \  
build-essential \  
automake \  
git \  
devscripts && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

