FROM ubuntu:14.04  
MAINTAINER Brennan Ashton <brennan@ombitron.com>  
  
ENV DISTRIB_CODENAME trusty  
ENV TOOLCHAIN_VERSION 4.9.3.2015q3-1trusty1  
  
RUN echo "deb http://ppa.launchpad.net/terry.guo/gcc-arm-embedded/ubuntu
$DISTRIB_CODENAME main" >> /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/terry.guo/gcc-arm-embedded/ubuntu
$DISTRIB_CODENAME main" >> /etc/apt/sources.list  
RUN apt-get update && apt-get install -y --force-yes gcc-arm-none-
eabi=$TOOLCHAIN_VERSION git && rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

