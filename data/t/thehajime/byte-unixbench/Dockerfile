# Basic build of frankenlibc with Docker  
FROM ubuntu:16.04  
MAINTAINER Hajime Tazaki <thehajime@gmail.com>  
  
  
RUN apt-get update && \  
apt-get install -y build-essential libx11-dev libgl1-mesa-dev \  
libxext-dev perl perl-modules make curl git vim netperf && \  
apt-get clean && \  
cpan install File::Which  
  
COPY . /usr/src/byte-unixbench  
RUN cd /usr/src/byte-unixbench/UnixBench && make  
WORKDIR /usr/src/byte-unixbench/UnixBench  
  

