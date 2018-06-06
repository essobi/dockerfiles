FROM nvidia/cuda:8.0-devel-ubuntu16.04  
MAINTAINER Florian Weik <fweik@icp.uni-stuttgart.de>  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
apt-utils \  
build-essential \  
clang-4.0 clang-tidy-4.0 \  
curl \  
cython \  
openmpi-bin \  
lcov \  
libfftw3-dev \  
libboost-dev libboost-serialization-dev libboost-mpi-dev libboost-filesystem-
dev libboost-test-dev \  
python python-numpy python-h5py python-enum \  
git \  
pep8 pylint\  
python-numpydoc \  
python-pyvtk \  
python-pip \  
python-pyface \  
libpython-dev \  
libhdf5-openmpi-dev \  
doxygen \  
vim \  
&& pip2 install --upgrade pip; pip2 install sphinx sphinxcontrib-bibtex
--upgrade \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /usr/local \  
&& curl -sL https://cmake.org/files/v3.8/cmake-3.8.2-Linux-x86_64.tar.gz | tar
--strip-components=1 -xz  
  
RUN cd /usr/src && \  
git clone https://github.com/thrust/thrust.git && \  
rm -r /usr/local/cuda/include/thrust && \  
ln -s /usr/src/thrust/thrust /usr/local/cuda/include/thrust  
  
ENV CC=/usr/bin/clang-4.0 CXX=/usr/bin/clang++-4.0 NVCC=/usr/bin/clang++-4.0  
  
COPY boost.patch /tmp/  
RUN cd /usr/include/boost && patch -p1 < /tmp/boost.patch  
  
RUN useradd -m espresso && usermod -a -G www-data espresso  
USER espresso  
WORKDIR /home/espresso  

