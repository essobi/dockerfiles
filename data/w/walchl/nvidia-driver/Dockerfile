FROM ubuntu:14.04  
MAINTAINER "Walter Chen-Hua Lu"  
ONBUILD \  
RUN apt-get update &&\  
apt-get -y install wget &&\  
apt-get clean  
  
ONBUILD \  
RUN mkdir -p /tmp/downloads &&\  
cd /tmp/downloads &&\  
wget -q http://us.download.nvidia.com/XFree86/Linux-x86_64/352.79/NVIDIA-
Linux-x86_64-352.79.run &&\  
sh NVIDIA-Linux-x86_64-*run -s -N --no-kernel-module &&\  
cd /tmp &&\  
rm -rf downloads  
  

