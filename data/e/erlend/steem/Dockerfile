FROM ubuntu:yakkety  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y git cmake g++ python3-dev autotools-dev libicu-dev \  
build-essential libbz2-dev libboost-all-dev libssl-dev libncurses5-dev \  
doxygen libreadline-dev dh-autoreconf libboost-dev  
  
WORKDIR /usr/src  
  
# Build secp256k1  
RUN git clone https://github.com/bitcoin/secp256k1 && \  
cd secp256k1 && \  
./autogen.sh && \  
./configure && \  
make && \  
./tests && \  
make install  
  
# Build steem  
RUN git clone https://github.com/steemit/steem && \  
cd steem && \  
git submodule update --init --recursive && \  
cmake -DCMAKE_BUILD_TYPE=Release \  
-DENABLE_CONTENT_PATCHING=OFF \  
-DLOW_MEMORY_NODE=ON && \  
make && \  
make install  
  
VOLUME /data  
WORKDIR /data  
CMD steemd --rpc-endpoint --seed-node=seed.steemed.net:2001 --seed-
node=52.74.152.79:2001  
  
# Cleanup  
RUN apt-get purge -y g++ cmake libncurses5-dev python3-dev autotools-dev git \  
libicu-dev libboost-dev libreadline-dev doxygen libbz2-dev libssl-dev && \  
apt-get autoremove --purge -y && \  
rm -rf /usr/src/* /var/lib/apt/lists/*  

