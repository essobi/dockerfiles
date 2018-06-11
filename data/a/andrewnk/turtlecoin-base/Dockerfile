FROM phusion/baseimage:0.10.0  
ARG TURTLECOIN_VERSION=v0.5.0  
ENV TURTLECOIN_VERSION=${TURTLECOIN_VERSION}  
  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
python-dev \  
gcc-4.9 \  
g++-4.9 \  
git cmake \  
libboost1.58-all-dev \  
librocksdb-dev  
  
RUN mkdir -p /tmp/turtlecoin  
  
WORKDIR /tmp/turtlecoin  
  
RUN git clone https://github.com/turtlecoin/turtlecoin.git . && \  
git checkout $TURTLECOIN_VERSION && \  
mkdir build  
  
WORKDIR /tmp/turtlecoin/build  
  
RUN cmake -DCMAKE_CXX_FLAGS="-g0 -Os -fPIC -std=gnu++11" ../ && \  
make -j$(nproc)  
  
RUN cp src/TurtleCoind /usr/local/bin/TurtleCoind && \  
cp src/walletd /usr/local/bin/walletd && \  
cp src/simplewallet /usr/local/bin/simplewallet && \  
cp src/miner /usr/local/bin/miner && \  
strip /usr/local/bin/TurtleCoind && \  
strip /usr/local/bin/walletd && \  
strip /usr/local/bin/simplewallet && \  
strip /usr/local/bin/miner  
  
WORKDIR /  
  
RUN rm -rf /tmp/turtlecoin && \  
apt-get remove -y build-essential python-dev gcc-4.9 g++-4.9 git cmake
libboost1.58-all-dev librocksdb-dev && \  
apt-get autoremove -y && \  
apt-get install -y \  
libboost-system1.58.0 \  
libboost-filesystem1.58.0 \  
libboost-thread1.58.0 \  
libboost-date-time1.58.0 \  
libboost-chrono1.58.0 \  
libboost-regex1.58.0 \  
libboost-serialization1.58.0 \  
libboost-program-options1.58.0 \  
libicu55  
  
RUN groupadd -g 1000 turtlecoin && \  
useradd -m -d /home/turtlecoin -r -u 1000 -g turtlecoin turtlecoin && \  
chmod -R 550 /usr/local/bin && \  
chown -R turtlecoin:turtlecoin /usr/local/bin  
  
WORKDIR /home/turtlecoin  

