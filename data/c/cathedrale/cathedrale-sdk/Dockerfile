FROM ubuntu:16.10  
  
MAINTAINER olivier.delannoy@gmail.com  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ yakkety universe" >>
/etc/apt/sources.list  
RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ yakkety universe" >>
/etc/apt/sources.list  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get update && \  
apt-get install -y --allow-unauthenticated \  
curl wget \  
cmake cmake-data \  
doxygen \  
make \  
build-essential \  
vim \  
git  

