FROM ubuntu:16.04  
MAINTAINER locke01  
  
# Install dependencies  
RUN \  
apt-get -qq update && apt-get -qq upgrade -y && \  
apt-get -qq install -y \  
build-essential \  
cmake \  
git \  
libgtk2.0-dev \  
pkg-config \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
curl && \  
apt-get autoclean && apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install OpenCV  
RUN \  
cd ~ && \  
git clone https://github.com/opencv/opencv.git && \  
  
cd ~/opencv && \  
mkdir build && \  
cd build && \  
  
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local .. && \  
  
make -j $(nproc) && \  
make install && \  
ldconfig && \  
  
rm -rf ~/opencv  

