FROM ubuntu:xenial  
MAINTAINER Florian Weik <fweik@icp.uni-stuttgart.de>  
ENV DEBIAN_FRONTEND noninteractive  
COPY build-and-install-scafacos.sh /tmp  
RUN apt-get update && apt-get install -y \  
apt-utils \  
cmake \  
build-essential \  
pkg-config \  
openmpi-bin libopenmpi-dev \  
gfortran \  
libfftw3-dev \  
libboost-dev libboost-serialization-dev libboost-mpi-dev libboost-filesystem-
dev libboost-test-dev \  
libgsl-dev \  
cython python python-numpy python-h5py python-enum \  
lcov \  
curl \  
git \  
pep8 pylint \  
python-vtk \  
python-pyface \  
libhdf5-openmpi-dev \  
libhdf5-openmpi-10:amd64 \  
libhdf5-10:amd64 \  
autoconf automake \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN bash /tmp/build-and-install-scafacos.sh  
  
RUN useradd -m espresso  
USER espresso  
WORKDIR /home/espresso  

