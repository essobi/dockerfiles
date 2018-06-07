FROM ubuntu:xenial  
MAINTAINER Kai Szuttor <kai@icp.uni-stuttgart.de>  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
apt-utils \  
cmake \  
curl \  
build-essential \  
openmpi-bin \  
libfftw3-dev \  
cython python python-numpy python-h5py python-coverage python-pip\  
git \  
pep8 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -m kaipy  
USER kaipy  
WORKDIR /home/kaipy  

