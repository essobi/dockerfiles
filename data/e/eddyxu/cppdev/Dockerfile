FROM ubuntu:14.04  
MAINTAINER Lei Xu <eddyxu@gmail.com>  
  
RUN apt-get update && \  
apt-get -y -qq install python-software-properties software-properties-common
&& \  
add-apt-repository ppa:ubuntu-toolchain-r/test && \  
apt-get update && \  
apt-get install -y -qq g++ cmake wget \  
unzip git libboost-all-dev libgoogle-glog-dev automake autoconf \  
autoconf-archive libtool libevent-dev libdouble-conversion-dev \  
libgflags-dev liblz4-dev liblzma-dev libsnappy-dev make zlib1g-dev \  
binutils-dev libjemalloc-dev libssl-dev libiberty-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
ENV CXX g++-4.9  
ENV CC gcc-4.9  
ENV PREFIX /usr/local  
# Build folly  
ADD build.sh /tmp/build.sh  
RUN /tmp/build.sh -folly -gmock && rm -rf /tmp/*  

