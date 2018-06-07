#FROM ubuntu:14.04  
FROM kaixhin/cuda:6.5  
  
MAINTAINER Axel Heitland <heitlaender@googlemail.com>  
  
# Start with Ubuntu base image  
#  
# Install wget and build-essential  
#RUN apt-get update && apt-get install -y \  
# build-essential \  
# wget  
#  
## Change to the /tmp directory  
#RUN cd /tmp && \  
## Download run file  
# wget
http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_linux.run
&& \  
## Make the run file executable and extract \  
# chmod +x cuda_*_linux.run && ./cuda_*_linux.run -extract=`pwd` && \  
## Install CUDA drivers (silent, no kernel)  
# ./NVIDIA-Linux-x86_64-*.run -s --no-kernel-module && \  
## Install toolkit (silent)  
# ./cuda-linux64-rel-*.run -noprompt && \  
## Clean up  
# rm -rf *  
#  
## Add to path  
#ENV PATH=/usr/local/cuda/bin:$PATH \  
#LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH  
#  
# —— CUDA base installation ready —  
  
# Install git, bc and dependencies  
RUN apt-get update && apt-get install -y \  
git \  
bc \  
libatlas-base-dev \  
libatlas-dev \  
libboost-all-dev \  
libopencv-dev \  
libprotobuf-dev \  
libgoogle-glog-dev \  
libgflags-dev \  
protobuf-compiler \  
libhdf5-dev \  
libleveldb-dev \  
liblmdb-dev \  
libsnappy-dev \  
python-pip  
  
RUN pip install Flask  
RUN pip install tornado  
RUN apt-get install python-numpy  
RUN pip install pandas  
RUN pip install PIL --allow-external PIL --allow-unverified PIL  
RUN pip install --upgrade
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.6.0-cp27-none-
linux_x86_64.whl  
  
# Clone Caffe repo and move into it  
RUN cd /root && git clone https://github.com/BVLC/caffe.git && cd caffe && \  
# Copy Makefile  
cp Makefile.config.example Makefile.config && \  
# Make  
make -j"$(nproc)" all && make pycaffe && make test  
  
# Set ~/caffe as working directory  
WORKDIR /root/caffe  

