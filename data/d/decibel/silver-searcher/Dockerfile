FROM ubuntu:14.04  
MAINTAINER Mike Christof <mhristof@gmail.com>  
  
ARG version=0.32.0  
RUN apt-get update && apt-get install -y build-essential automake pkg-config
libpcre3-dev zlib1g-dev liblzma-dev wget  
RUN wget
https://github.com/ggreer/the_silver_searcher/archive/${version}.tar.gz &&\  
tar xf ${version}.tar.gz &&\  
cd the_silver_searcher-${version} &&\  
./build.sh &&\  
make install  
  

