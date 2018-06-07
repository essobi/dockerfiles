FROM ubuntu:16.04  
  
MAINTAINER Jeffreyy Chun-Hui Yu  
  
# install the system requirement  
RUN \  
apt-get update -qy --fix-missing \  
&& apt-get install -qy wget git curl zlib1g-dev libncurses5-dev bzip2 make g++
gcc  
  
WORKDIR /opt  
  
# BWA installation  
RUN \  
wget http://downloads.sourceforge.net/project/bio-bwa/bwa-0.7.15.tar.bz2 \  
&& tar jxvf bwa-0.7.15.tar.bz2 \  
&& mv bwa-0.7.15 bwa \  
&& cd bwa \  
&& make  
  
# reduce image size  
RUN \  
apt-get autoremove -y \  
&& rm -f /opt/bwa-0.7.15.tar.bz2 \  
&& rm -rf /var/lib/apt  
  
# set environment  
ENV
PATH=/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/opt/bwa:/opt/bwa/bwakit:$PATH  
  
WORKDIR /root  
  

