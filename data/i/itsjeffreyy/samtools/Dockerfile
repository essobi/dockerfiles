ROM ubuntu:16.04  
  
MAINTAINER Jeffreyy Chun-Hui Yu  
  
# install the system requirement  
RUN apt update --fix-missing \  
&& apt install -q -y wget g++ gcc make bzip2 libncurses5-dev zlib1g-dev git  
  
# samtools installation  
RUN \  
wget
http://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
\  
&& tar -xjvf samtools-1.3.1.tar.bz2 -C /opt \  
&& cd /opt/ \  
&& mv samtools-1.3.1 samtools \  
&& cd samtools \  
&& ./configure \  
&& make \  
&& cd htslib-1.3.1/ \  
&& ./configure \  
&& make \  
&& rm -rf /samtools-1.3.1.tar.bz2  
  
# reduce image size  
RUN apt-get remove -q -y zlib1g-dev libncurses5-dev wget g++ gcc make bzip2 \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt  
  
# set environment  
ENV
PATH=/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/opt/samtools/:/opt/samtools/misc  
  
WORKDIR /root/  

