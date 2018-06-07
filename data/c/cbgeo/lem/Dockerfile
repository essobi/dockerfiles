FROM fedora:26  
MAINTAINER Krishna Kumar <kks32@cam.ac.uk>  
  
# Update to latest packages, remove vim-minimal & Install Git, GCC, Clang,
Autotools and VIM  
RUN dnf update -y && \  
dnf remove -y vim-minimal python sqlite && \  
dnf install -y boost boost-devel clang cmake cppcheck dnf-plugins-core
eigen3-devel findutils gcc gcc-c++ \  
git gmsh gmsh-devel hdf5 hdf5-devel kernel-devel \  
make sqlite sqlite-devel tar tbb tbb-devel valgrind vim \  
voro++ voro++-devel vtk vtk-devel wget && \  
dnf clean all  
  
# Install CUDA  
RUN wget
https://developer.download.nvidia.com/compute/cuda/repos/fedora25/x86_64/cuda-
repo-fedora25-9.1.85-1.x86_64.rpm && \  
dnf install -y ./cuda-repo-fedora25-9.1.85-1.x86_64.rpm && \  
dnf install -y cuda && \  
dnf clean all  
  
# Install MKL  
RUN dnf config-manager --add-repo https://yum.repos.intel.com/mkl/setup/intel-
mkl.repo && \  
rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-
PRODUCTS-2019.PUB && \  
dnf install -y intel-mkl  
  
# Create a user cbgeo  
RUN useradd cbgeo  
USER cbgeo  
  
# Configure MKL  
RUN echo "source /opt/intel/bin/compilervars.sh -arch intel64 -platform linux"
>> ~/.bashrc  
RUN echo "source /opt/intel/mkl/bin/mklvars.sh intel64" >> ~/.bashrc  
  
# Create a research directory and clone git repo of lbmdem code  
RUN mkdir -p /home/cbgeo/research && \  
cd /home/cbgeo/research  
# && \  
# git clone https://github.com/cb-geo/lem.git  
# Done  
#WORKDIR /home/cbgeo/research/lem  
WORKDIR /home/cbgeo/research/  
  
RUN /bin/bash "$@"  

