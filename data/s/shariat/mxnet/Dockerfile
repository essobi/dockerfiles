FROM ubuntu:16.04  
MAINTAINER Ali Shariat <shariat@gmail.com>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
libopenblas-dev \  
libopencv-dev \  
python-dev \  
python-pip \  
python-numpy \  
python-setuptools \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Clone MXNet repo and move into it  
RUN git clone \--recursive https://github.com/dmlc/mxnet /mxnet  
  
RUN cd /mxnet && make -j"$(nproc)" USE_DIST_KVSTORE=1 USE_BLAS=openblas && \  
cd /mxnet/python && python setup.py install  
  
# Set /mxnet as working directory  
WORKDIR "/mxnet"  

