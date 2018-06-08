FROM debian:jessie  
MAINTAINER Jan-Gerd Tenberge <jan-gerd.tenberge@uni-muenster.de>  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
python \  
python-numpy \  
libeigen3-dev \  
clang \  
zlib1g-dev \  
libqt4-opengl-dev \  
libgl1-mesa-dev \  
git \  
ca-certificates  
RUN mkdir /mrtrix  
RUN git clone https://github.com/MRtrix3/mrtrix3.git --depth 1 --branch
3.0_RC2 /mrtrix  
WORKDIR /mrtrix  
ENV CXX=/usr/bin/clang++  
RUN ./configure  
RUN ./build  
ENV PATH=/mrtrix/release/bin:/mrtrix/scripts/:$PATH  

