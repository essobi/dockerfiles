FROM ubuntu:xenial  
MAINTAINER Vasileios Karavasilis <vasileioskaravasilis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update \  
&& apt-get -qqy install \  
build-essential \  
cmake \  
libboost-all-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT /bin/bash  

