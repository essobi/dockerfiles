FROM ubuntu:latest  
  
MAINTAINER Martin Soto <donsoto@gmail.com>  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update \  
&& apt-get install -y \  
build-essential \  
curl \  
git \  
libsnappy-dev \  
zlib1g-dev \  
libbz2-dev \  
libgflags-dev \  
python-software-properties \  
python2.7 \  
python2.7-dev \  
software-properties-common \  
&& apt-get clean  
  
# Build and install the RocksDB library.  
RUN mkdir /build \  
&& cd /build \  
&& git clone https://github.com/facebook/rocksdb.git \  
&& cd rocksdb \  
&& INSTALL_PATH=/usr make install-shared \  
&& rm -rf /build  
  
# Install a recent Pip.  
RUN curl https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py \  
&& python /tmp/get-pip.py \  
&& rm /tmp/get-pip.py  
# RocksDB Python bindings.  
RUN pip install pyrocksdb  
  

