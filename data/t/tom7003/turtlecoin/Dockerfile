FROM debian:9 as builder  
  
#VOLUME ["/var/lib/turtlecoind", "/home/turtlecoin","/var/log/turtlecoind"]  
#ARG TURTLECOIN_VERSION=v0.2.2  
# install build dependencies  
# checkout the latest tag  
# build and install  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
gdb \  
python-dev \  
gcc \  
g++\  
git \  
cmake \  
libboost-all-dev \  
librocksdb-dev && \  
git clone https://github.com/turtlecoin/turtlecoin.git /opt/turtlecoin && \  
cd /opt/turtlecoin && \  
mkdir build && \  
cd build && \  
export CXXFLAGS="-w -std=gnu++11" && \  
#cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo .. && \  
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_FLAGS="-fassociative-math"
-DCMAKE_CXX_FLAGS="-fassociative-math" -DSTATIC=true -DDO_TESTS=OFF .. && \  
make -j$(nproc)  
  
FROM debian:9  
RUN mkdir -p /usr/local/bin  
WORKDIR /usr/local/bin  
COPY \--from=builder /opt/turtlecoin/build/src/TurtleCoind .  
COPY \--from=builder /opt/turtlecoin/build/src/walletd .  
COPY \--from=builder /opt/turtlecoin/build/src/simplewallet .  
COPY \--from=builder /opt/turtlecoin/build/src/miner .  
RUN mkdir -p /var/lib/turtlecoind  
WORKDIR /var/lib/turtlecoind  
ADD https://github.com/turtlecoin/checkpoints/raw/master/checkpoints.csv
/var/lib/turtlecoind  
ENTRYPOINT ["/usr/local/bin/TurtleCoind"]  
CMD ["--no-console","--data-dir","/var/lib/turtlecoind","--rpc-bind-
ip","0.0.0.0","--rpc-bind-port","11898","--p2p-bind-port","11897","--enable-
cors=*","--enable_blockexplorer","--load-
checkpoints","/var/lib/turtlecoind/checkpoints.csv"]  

