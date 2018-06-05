# A bleeding edge Ubuntu 14.04 image for compiling C++11 OpenGL projects.  
FROM ubuntu:14.04  
MAINTAINER andystanton  
  
# update and install dependencies  
RUN apt-get update \  
&& apt-get install -y \  
software-properties-common \  
wget \  
&& echo 'deb http://llvm.org/apt/trusty/ llvm-toolchain-trusty-3.4 main' >>
/etc/apt/sources.list \  
&& wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key|sudo apt-key add - \  
&& add-apt-repository -y ppa:ubuntu-toolchain-r/test \  
&& apt-get update \  
&& apt-get install -y \  
make \  
git \  
curl \  
ruby \  
&& apt-get install -y \  
xorg-dev \  
libglu1-mesa-dev \  
&& apt-get install -y \  
gcc-4.9 g++-4.9 gcc-4.9-base \  
gcc-4.8 g++-4.8 gcc-4.8-base \  
gcc-4.7 g++-4.7 gcc-4.7-base \  
gcc-4.6 g++-4.6 gcc-4.6-base \  
clang-3.4 lldb-3.4 \  
&& gem install rake \  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \  
&& update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100  
  
# build cmake  
RUN curl -O http://www.cmake.org/files/v3.0/cmake-3.0.2.tar.gz \  
&& tar -xvf cmake-3.0.2.tar.gz  
WORKDIR cmake-3.0.2  
RUN ./bootstrap \  
&& make \  
&& make install  

