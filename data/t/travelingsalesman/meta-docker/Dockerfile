# This is a Dockerfile for getting started with META  
# https://www.coursera.org/learn/text-mining/home/welcome  
# META is installed in /code/meta  
FROM ubuntu:trusty  
  
ENV META_VER=2.4.2  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get clean  
  
# add the ppa for cmake  
RUN add-apt-repository ppa:george-edison55/cmake-3.x  
RUN apt-get update && \  
apt-get install -y g++ \  
cmake \  
libicu-dev \  
git \  
libjemalloc-dev \  
zlib1g-dev \  
pxz \  
liblzma-dev \  
libicu-dev && \  
apt-get clean  
  
RUN mkdir -p /code && \  
cd code && \  
git clone --recursive https://github.com/meta-toolkit/meta.git && \  
cd /code/meta && \  
git checkout tags/v${META_VER} && \  
git submodule update \--recursive && \  
mkdir -p build && \  
cd build && \  
cmake .. && \  
make -j4  

