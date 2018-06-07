FROM ubuntu:trusty  
  
MAINTAINER Milos Prchlik <happz@happz.cz>  
  
RUN apt-get update && apt-get install -y build-essential lsb-release git make
ninja-build wget && apt-get clean  
  
RUN wget --no-check-certificate -O /tmp/cmake-3.5.2.tar.gz
http://www.cmake.org/files/v3.5/cmake-3.5.2.tar.gz \  
&& tar xf /tmp/cmake-3.5.2.tar.gz -C /tmp \  
&& cd /tmp/cmake-3.5.2 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd \  
&& rm -rf /tmp/cmake-3.5.2 /tmp/cmake-3.5.2.tar.gz  
  
RUN mkdir -p /llvm-build  
ADD Makefile /llvm-build/Makefile  

