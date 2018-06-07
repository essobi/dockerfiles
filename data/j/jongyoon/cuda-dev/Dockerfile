# Start from cuDNN base image  
FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
MAINTAINER JongYoon Lim <jongyoon@apache.org>  
  
# Install dependencies  
#ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
# apt-utils \  
git \  
wget \  
bc \  
cmake \  
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
python-dev \  
python-pip \  
python-numpy \  
gfortran > /dev/null  
# Install NCCL for multi-GPU communication  
ENV NCCL libnccl1_1.3.4-1.cuda8.0_amd64.deb  
ENV NCCL_DEV libnccl-dev_1.3.4-1.cuda8.0_amd64.deb  
RUN wget https://github.com/NVIDIA/nccl/releases/download/v1.3.4-1/${NCCL} &&
\  
dpkg -i ${NCCL} && \  
rm ${NCCL} && \  
wget https://github.com/NVIDIA/nccl/releases/download/v1.3.4-1/${NCCL_DEV} &&
\  
dpkg -i ${NCCL_DEV} && \  
rm ${NCCL_DEV}  

