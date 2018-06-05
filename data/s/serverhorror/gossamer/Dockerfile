FROM ubuntu:16.04  
  
LABEL maintainer "Martin Marcher <martin@marcher.name>"  
  
RUN export DEBIAN_FRONTEND="noninteractive" && \  
apt-get \--quiet=2 \--yes update && \  
apt-get \--quiet=2 \--yes upgrade && \  
apt-get \--quiet=2 \--yes install \  
g++ cmake libboost-all-dev pandoc \  
zlib1g-dev libbz2-dev libsqlite3-dev \  
git && \  
git clone https://github.com/data61/gossamer.git && \  
cd gossamer && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make test && \  
make install && \  
apt-get remove \--quiet=2 \--yes --purge \  
libboost-all-dev zlib1g-dev libbz2-dev libsqlite3-dev && \  
apt-get clean && \  
cd ~ && \  
rm -rf gossamer && \  
echo "all done"  

