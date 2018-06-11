FROM ubuntu:16.04  
  
RUN apt-get update -q && apt-get -qy install \  
qt5-default qt5-qmake qtbase5-dev-tools qttools5-dev-tools \  
build-essential libboost-dev libboost-system-dev \  
libboost-filesystem-dev libboost-program-options-dev libboost-thread-dev \  
libssl-dev libdb++-dev git libminiupnpc-dev libzmq3-dev  
  
ADD . /root/wyvern  
  
RUN cd /root/wyvern/src && mkdir -p obj/zmq && make -f makefile.unix -j
$(nproc)  

