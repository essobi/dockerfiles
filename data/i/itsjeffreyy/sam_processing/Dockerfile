# Base image ubuntu:16.04  
FROM ubuntu:16.04  
# Author  
MAINTAINER Jeffreyy Chun-Hui Yu  
  
# install the system requirement  
RUN \  
apt update --fix-missing \  
&& apt install -q -y wget g++ gcc make bzip2 git autoconf automake make g++
gcc build-essential zlib1g-dev libgsl0-dev perl curl git wget unzip tabix
libncurses5-dev python  
  
WORKDIR /opt  
  
# install samtools and sambamba  
# samtools part  
RUN \  
wget
http://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
\  
&& tar -xjvf samtools-1.3.1.tar.bz2 -C /opt \  
&& mv samtools-1.3.1 samtools \  
&& cd samtools \  
&& ./configure \  
&& make \  
&& cd htslib-1.3.1/ \  
&& ./configure \  
&& make  
  
# sambamba part  
RUN \  
wget https://github.com/ldc-
developers/ldc/releases/download/v0.17.1/ldc2-0.17.1-linux-x86_64.tar.xz \  
&& tar xJf ldc2-0.17.1-linux-x86_64.tar.xz  
  
ENV PATH=/opt/ldc2-0.17.1-linux-x86_64/bin/:$PATH  
ENV LIBRARY_PATH=/opt/ldc2-0.17.1-linux-x86_64/lib/  
  
RUN \  
git clone --recursive https://github.com/lomereiter/sambamba.git \  
&& cd /opt/sambamba \  
&& make sambamba-ldmd2-64  
  
# clean tar balls  
RUN \  
rm -f /opt/samtools-1.3.1.tar.bz2 \  
&& rm -f /opt/ldc2-0.17.1-linux-x86_64.tar.xz \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# set evironment pathway  
ENV
PATH=/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/opt/samtools/:/opt/samtools/misc:/opt/sambamba/build/:$PATH  
  
# set work path  
WORKDIR /root  

