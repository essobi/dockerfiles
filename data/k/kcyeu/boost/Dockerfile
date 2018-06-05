FROM ubuntu:trusty  
MAINTAINER Kuo-Cheng Yeu <kmd@mikuru.tw>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update \  
&& apt-get -qqy install \  
libboost-all-dev \  
g++ \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT /bin/bash  
  

