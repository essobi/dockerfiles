FROM ubuntu:16.04  
MAINTAINER Timo Taskinen <timo.taskinen@iki.fi>  
  
RUN apt-get update && apt-get install -y \  
cmake \  
build-essential \  
libboost-all-dev \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /opt; git clone -b Linux https://github.com/nicehash/nheqminer.git  
RUN cd /opt/nheqminer/cpu_xenoncat/Linux/asm/; sh assemble.sh  
RUN cd /opt/nheqminer/Linux_cmake/nheqminer_cpu; cmake .; make -j $(nproc)  
  
ENTRYPOINT ["/opt/nheqminer/Linux_cmake/nheqminer_cpu/nheqminer_cpu -l
equihash.hk.nicehash.com:3357 -u 1LWF6LsCgUktAb8szrBYQs8Wz8FAx37QfF.work1 -t
2"]  

