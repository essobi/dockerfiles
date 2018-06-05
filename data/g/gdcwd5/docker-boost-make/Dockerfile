FROM ubuntu:trusty  
MAINTAINER Geoffrey Cline <gdcwd5@mst.edu>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update \  
&& apt-get -qqy install \  
libboost-all-dev \  
g++ \  
vim \  
make \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT /bin/bash  
  

