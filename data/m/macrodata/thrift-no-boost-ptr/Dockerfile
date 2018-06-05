FROM ubuntu:latest  
MAINTAINER YI-HUNG JEN <yihungjen@gmail.com>  
  
# install workspace dependency  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
automake \  
bison \  
bundler \  
flex \  
g++ \  
git \  
gem \  
libboost-dev \  
libboost-test-dev \  
libboost-program-options-dev \  
libboost-system-dev \  
libboost-filesystem-dev \  
libevent-dev \  
libglib2.0-dev \  
libssl-dev \  
libtool \  
openjdk-7-jdk \  
pkg-config \  
php5-cli \  
php5-dev \  
python \  
python-dev \  
rake \  
ruby-full \  
ruby-dev \  
zlib1g-dev  
  
# get instance of thrift from  
COPY . /thrift  
  
# settle in on the thrift source root  
WORKDIR /thrift  
  
# pew pew pew  
RUN ./bootstrap.sh  
RUN ./configure CXXFLAGS='-O3 -std=c++0x' \--prefix=/target  
RUN make  
  
CMD make install  

