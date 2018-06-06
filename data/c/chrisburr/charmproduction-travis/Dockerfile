FROM ubuntu:12.04  
MAINTAINER Chris Burr  
  
# Replace sh with bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install ROOT's dependencies  
RUN apt-get update && apt-get -y install git dpkg-dev make g++ gcc binutils \  
libx11-dev libxpm-dev libxft-dev libxext-dev gfortran libssl-dev \  
libpcre3-dev xlibmesa-glu-dev libglew1.5-dev libftgl-dev \  
libmysqlclient-dev libfftw3-dev cfitsio-dev graphviz-dev \  
libavahi-compat-libdnssd-dev libldap2-dev python-dev libxml2-dev \  
libkrb5-dev libgsl0-dev libqt4-dev wget  
  
# Update gcc to 4.8  
RUN apt-get -y install python-software-properties && \  
add-apt-repository -y ppa:ubuntu-toolchain-r/test && \  
apt-get update && \  
apt-get -y install gcc-4.8 g++-4.8 && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20 && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 20 && \  
update-alternatives --config gcc && \  
update-alternatives --config g++  
  
# Install anaconda  
RUN wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
-O miniconda.sh && \  
bash miniconda.sh -b -p $HOME/miniconda && \  
export PATH="$HOME/miniconda/bin:$PATH" && \  
hash -r && \  
conda create --yes -n test-environment python=2.7 flake8 numpy mock scipy
matplotlib && \  
source activate test-environment && \  
/usr/bin/yes | pip install uncertainties jug  
  
# cmake is too old in the Ubuntu repositories so install a newer version from
source  
RUN export PATH="$HOME/miniconda/bin:$PATH" && \  
hash -r && \  
source activate test-environment && \  
wget --no-check-certificate https://cmake.org/files/v3.4/cmake-3.4.3.tar.gz &&
\  
tar -xf cmake-3.4.3.tar.gz && \  
cd cmake-3.4.3 && \  
./bootstrap && \  
make && \  
make install && \  
cd .. && \  
rm -r cmake-3.4.3 cmake-3.4.3.tar.gz  
  
# Build xrootd  
RUN export PATH="$HOME/miniconda/bin:$PATH" && \  
hash -r && \  
source activate test-environment && \  
wget http://xrootd.org/download/v4.3.0/xrootd-4.3.0.tar.gz && \  
tar -xf xrootd-4.3.0.tar.gz && \  
mkdir build && \  
cd build && \  
cmake ../xrootd-4.3.0 -DENABLE_PERL=FALSE && \  
make && \  
make install && \  
cd .. && \  
rm -r xrootd-4.3.0 xrootd-4.3.0.tar.gz build  
  
# Build ROOT  
RUN export PATH="$HOME/miniconda/bin:$PATH" && \  
hash -r && \  
source activate test-environment && \  
wget --no-check-certificate
https://root.cern.ch/download/root_v6.04.14.source.tar.gz && \  
tar -xf root_v6.04.14.source.tar.gz && \  
mkdir build && \  
cd build && \  
cmake ../root-6.04.14 && \  
cmake --build . && \  
cmake --build . --target install && \  
cd .. && \  
rm -rf root-6.04.14 build root_v6.04.14.source.tar.gz  

