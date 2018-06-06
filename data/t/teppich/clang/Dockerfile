FROM ubuntu:17.10  
  
MAINTAINER Tobias Kölling <tobias.koelling@physik.uni-muenchen.de>  
  
RUN apt-get update && apt-get install -y \  
git \  
make \  
cmake \  
clang \  
libtool \  
python \  
python-dev \  
libboost-all-dev \  
libeigen3-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN update-alternatives --set cc /usr/bin/clang \  
&& update-alternatives --set c++ /usr/bin/clang++  

