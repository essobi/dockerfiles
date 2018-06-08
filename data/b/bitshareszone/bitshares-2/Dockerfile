FROM bitshareszone/boost:1.57  
MAINTAINER Fabian Schuh <Fabian@cryptonomex.com>  
  
## Core Utilities  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y build-essential \  
gcc-4.9 \  
g++-4.9 \  
cmake \  
make \  
libbz2-dev \  
libdb++-dev \  
libdb-dev \  
libssl-dev \  
openssl \  
libreadline-dev \  
autoconf \  
libtool \  
git \  
autotools-dev \  
libbz2-dev \  
libicu-dev \  
python-dev \  
wget \  
libncurses5-dev \  
doxygen  
  
RUN git clone --recursive https://github.com/bitshares/bitshares-2
/bitshares-2-git  
  
RUN mkdir /build && \  
cd /build/ && \  
CC=gcc-4.9 CXX=g++-4.9 cmake -DBOOST_ROOT="/opt/boost_1_57_0"
-DCMAKE_BUILD_TYPE=Release /bitshares-2-git && \  
make || make -j 1 && \  
mkdir /bitshares-2 && \  
cp -r /build/programs /bitshares-2/ && \  
rm -rf /bitshares-2-git /build  
  

