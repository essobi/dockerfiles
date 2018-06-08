# Installs CUDA.  
# Inspiration derived from tleyden5iwx/ubuntu-cuda.  
# Also from https://github.com/BVLC/caffe/wiki/Caffe-on-
EC2-Ubuntu-14.04-Cuda-7 .  
FROM ubuntu:14.04.2  
MAINTAINER Shannon Quinn "magsol@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get -y install wget build-essential  
RUN wget
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-
repo-ubuntu1404_7.0-28_amd64.deb && \  
dpkg -i cuda-repo-ubuntu1404_7.0-28_amd64.deb && apt-get -y update  
  
# Note that we do upgrade and not dist-upgrade so that we don't install  
# new kernels; this script will install the nvidia driver in the *currently  
# running* kernel.  
RUN apt-get upgrade -y && apt-get install -y opencl-headers protobuf-compiler
\  
libprotoc-dev libboost-all-dev libleveldb-dev hdf5-tools libhdf5-serial-dev \  
libsnappy-dev libsnappy1 libatlas-base-dev cmake libstdc++6-4.8-dbg \  
libgoogle-glog0 libgoogle-glog-dev libgflags-dev liblmdb-dev git gfortran && \  
apt-get clean  
RUN apt-get install -y linux-image-extra-`uname -r` linux-headers-`uname -r` \  
linux-image-`uname -r`  
  
# Install CUDA.  
RUN apt-get install -y cuda && apt-get clean && rm cuda-repo-
ubuntu1404_7.0-28_amd64.deb  
  
# Need to put cuda on the linker path. This may not be the best way, but it
works.  
RUN echo '/usr/local/cuda/lib64' > /etc/ld.so.conf.d/cuda_hack.conf && \  
ldconfig /usr/local/cuda/lib64  
ENV PATH=$PATH:/usr/local/cuda/bin  

