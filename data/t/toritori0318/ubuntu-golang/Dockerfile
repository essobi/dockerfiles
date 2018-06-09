FROM golang:latest  
  
MAINTAINER TSUYOSHI TORII toritori0318  
  
# packages  
RUN apt-get -q -y update \  
&& apt-get -q -y install git wget curl tar gzip rsync \  
&& apt-get -q -y clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/*  

