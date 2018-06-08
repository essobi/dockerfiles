FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
build-essential \  
clang-3.6 \  
git \  
libgl1-mesa-dev \  
libglew-dev \  
libtool \  
nasm \  
wget \  
xorg-dev \  
&& rm -rf /var/lib/apt/lists/*  
RUN ln -s /usr/bin/clang-3.6 /usr/bin/clang \  
&& ln -s /usr/bin/clang++-3.6 /usr/bin/clang++  
RUN wget http://www.cmake.org/files/v3.4/cmake-3.4.0.tar.gz \  
&& tar -xvzf cmake-3.4.0.tar.gz \  
&& cd cmake-3.4.0/ \  
&& ./configure \  
&& make \  
&& make install  

