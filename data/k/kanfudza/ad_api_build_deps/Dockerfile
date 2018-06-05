#FROM gcc:4.8  
FROM ubuntu:14.04  
RUN echo "MY GCC 4.8 image"  
  
# update and install cmake x11 unzip  
RUN \  
apt-get update && \  
apt-get install wget build-essential unzip bzip2 git libx11-dev curl -y && \  
wget https://cmake.org/files/v3.7/cmake-3.7.1.tar.gz && \  
tar xvf cmake-3.7.1.tar.gz && \  
cd cmake-3.7.1 && \  
./configure && \  
make && \  
make install && \  
cd .. && rm -rf cmake-3.7.1 && \  
rm cmake-3.7.1.tar.gz && \  
apt-get -y clean all && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["cmake --version"]  

