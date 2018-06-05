FROM ubuntu:14.04.1  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update  
#RUN apt-get -y install language-pack-en-base  
#RUN dpkg-reconfigure locales  
RUN apt-get -y install software-properties-common wget  
RUN wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | apt-key add -  
RUN add-apt-repository "deb http://llvm.org/apt/trusty/ llvm-toolchain-
trusty-3.5-binaries main" && add-apt-repository -y ppa:ethereum/ethereum &&
add-apt-repository -y ppa:ethereum/ethereum-dev  
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y build-
essential g++-4.8 git cmake libboost-all-dev automake unzip libgmp-dev libtool
libleveldb-dev yasm libminiupnpc-dev libreadline-dev scons libncurses5-dev
libcurl4-openssl-dev wget libjsoncpp-dev libargtable2-dev libcryptopp-dev
libjson-rpc-cpp-dev libmicrohttpd-dev clang-3.5 lldb-3.5  
RUN mkdir -p /usr/src  
WORKDIR /usr/src/  
RUN git clone https://github.com/ethereum/cpp-ethereum && cd cpp-ethereum &&
git checkout master && mkdir build && cd build && cmake .. -DHEADLESS=1 &&
make -j2  
ADD init.sh /usr/src/init.sh  
EXPOSE 30303  
CMD chmod a+x /usr/src/init.sh && /usr/src/init.sh  

