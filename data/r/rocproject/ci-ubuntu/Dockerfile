FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
# compilers  
RUN apt-get install -y \  
g++ \  
g++-4.8 \  
g++-4.9 \  
g++-5 \  
clang-3.6 \  
clang-3.7  
# tools  
RUN apt-get install -y \  
pkg-config \  
scons \  
gengetopt \  
doxygen \  
graphviz  
  
# dependencies  
RUN apt-get install -y \  
libuv1-dev \  
libsox-dev \  
libcpputest-dev \  
intltool \  
m4 \  
make \  
cmake  

