FROM ubuntu:16.04  
MAINTAINER kmd.geek  
  
RUN apt-get update && \  
apt-get install -y git cmake build-essential libboost-all-dev && \  
cd /tmp && \  
git clone -b Linux https://github.com/nicehash/nheqminer.git && \  
cd nheqminer/cpu_xenoncat/Linux/asm/ && \  
sh assemble.sh && \  
cd ../../../Linux_cmake/nheqminer_cpu_xenoncat && \  
cmake . && \  
make -j $(nproc) && \  
cp nheqminer_cpu_xenoncat /nheqminer && \  
rm -rf /tmp/* && \  
chmod +x /nheqminer  
  
WORKDIR /  
CMD ["/nheqminer -h"]  

