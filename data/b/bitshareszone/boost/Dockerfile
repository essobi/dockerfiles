FROM ubuntu:15.04  
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
wget  
  
## Boost 1.57  
RUN wget -O /boost_1_57_0.tar.bz2 -c
'http://sourceforge.net/projects/boost/files/boost/1.57.0/boost_1_57_0.tar.bz2/download'
&& \  
tar xjf /boost_1_57_0.tar.bz2 && \  
cd /boost_1_57_0/ && \  
./bootstrap.sh "--prefix=/opt/boost_1_57_0" && \  
./b2 install && \  
rm -rf /boost_1_57_0.tar.bz2 /boost_1_57_0  

