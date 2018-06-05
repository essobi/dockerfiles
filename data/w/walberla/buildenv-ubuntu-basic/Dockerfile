FROM nvidia/cuda:8.0-devel-ubuntu16.04  
MAINTAINER Martin Bauer "martin.bauer@fau.de"  
# OpenSSH is required to run MPI applications  
RUN apt-get update && apt-get install -y \  
automake \  
build-essential \  
cmake \  
curl \  
doxygen \  
git \  
graphviz \  
libboost-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libboost-regex-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libbz2-dev \  
libopenmpi-dev \  
openmpi-bin \  
openmpi-common \  
openssh-client \  
python3-dev \  
python3-numpy \  
libboost-python-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD install*.sh /root/  
  
RUN /root/install_ccache.sh  
ENV CCACHE_DIR=/ccache  
  
RUN /root/install_metis.sh  
ENV CMAKE_PREFIX_PATH=/opt/metis:$CMAKE_PREFIX_PATH  
  
RUN /root/install_parmetis.sh  
ENV CMAKE_PREFIX_PATH=/opt/parmetis:$CMAKE_PREFIX_PATH  
  
RUN /root/install_openmesh.sh  
ENV CMAKE_PREFIX_PATH=/opt/openmesh:$CMAKE_PREFIX_PATH  
  
RUN /root/install_fftw-3.3.4_gcc.sh  
RUN /root/install_pfft-1.0.8-alpha_gcc.sh  
ENV CMAKE_PREFIX_PATH=/opt/fftw-3.3.4:/opt/pfft-1.0.8-alpha:$CMAKE_PREFIX_PATH  
  
ENV WALBERLA_BUILD_WITH_CUDA=1  
ENV WALBERLA_BUILD_WITH_PYTHON=1  

