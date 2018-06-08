FROM nvidia/cuda:8.0-runtime-ubuntu16.04  
MAINTAINER Austin Robison <austin.robison@gmail.com>  
  
ADD ccminer .  
  
RUN apt-get update && apt-get install -y \  
libcurl3 \  
libgomp1  
  
CMD ./ccminer --algo skunk -o stratum+tcp://sigt.suprnova.cc:7106 -u
arobison.master -p master  
  

