FROM centos:7  
MAINTAINER Florian Weik <fweik@icp.uni-stuttgart.de>  
RUN yum -y install epel-release && yum -y install \  
gcc gcc-c++ make \  
cmake3 \  
openmpi-devel \  
fftw-devel \  
boost-devel boost-serialization-devel boost-openmpi-devel boost-filesystem-
devel boost-test-devel \  
python numpy h5py\  
git \  
python-pep8 \  
python2-pip \  
python2-enum \  
python-devel \  
hdf5-openmpi-devel \  
zlib-devel \  
which \  
vim \  
&& yum clean all \  
&& ln -s /usr/bin/cmake3 /usr/bin/cmake \  
&& pip2 install --upgrade pip; pip2 install cython pylint  
RUN useradd -m espresso  
USER espresso  
WORKDIR /home/espresso  

