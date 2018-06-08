FROM ubuntu:trusty  
MAINTAINER Paweł Jasiak <pj1031999@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
gcc \  
g++ \  
gcc-multilib \  
g++-multilib \  
build-essential \  
vim \  
valgrind \  
gdb \  
fpc \  
libc6-dev \  
unzip \  
wget \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget --no-check-certificate -O oitimetool.zip
https://github.com/olimpiada/oitimetool-bin/archive/master.zip \  
&& unzip oitimetool.zip \  
&& wget --no-check-certificate
http://software.intel.com/sites/landingpage/pintool/downloads/pin-2.14-71313-gcc.4.4.7-linux.tar.gz
\  
&& tar xf pin-2.14-71313-gcc.4.4.7-linux.tar.gz \  
&& rm pin-2.14-71313-gcc.4.4.7-linux.tar.gz \  
&& mv pin-2.14-71313-gcc.4.4.7-linux ./oitimetool-bin-master/ \  
&& mv ./oitimetool-bin-master /root/oitimetool \  
&& rm oitimetool.zip \  
&& echo "CC := gcc" >> ~/Makefile \  
&& echo "CXX := g++" >> ~/Makefile \  
&& echo "CFLAGS := -O2 -m32 -static -lm -std=gnu99" >> ~/Makefile \  
&& echo "CXXFLAGS := -O2 -m32 -static -lm -std=c++11" >> ~/Makefile  
  
  
WORKDIR /root  
ENTRYPOINT /bin/bash  

