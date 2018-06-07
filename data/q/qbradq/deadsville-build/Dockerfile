# Image configuration  
FROM ubuntu:trusty  
MAINTAINER qbradq@gmail.com  
  
# Build environment  
RUN apt-get -qq update && \  
apt-get -qq install \  
apt-utils \  
python-software-properties \  
software-properties-common \  
&& \  
add-apt-repository -y ppa:george-edison55/cmake-3.x && \  
add-apt-repository -y ppa:ubuntu-toolchain-r/test && \  
apt-get -qq update && \  
apt-get -qq install \  
clang-3.9 \  
cmake \  
g++-5 \  
gcc-5 \  
libsdl2-dev \  
libsdl2-image-dev \  
&& \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 1000 && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 1000 && \  
update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.9 1000 &&
\  
update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.9
1000  

