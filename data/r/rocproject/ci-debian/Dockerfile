FROM debian:stable  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
# compilers  
RUN apt-get install -y g++  
  
# tools  
RUN apt-get install -y \  
pkg-config \  
scons \  
gengetopt \  
doxygen \  
graphviz  
  
# dependencies  
RUN apt-get install -y \  
libsox-dev \  
libtool \  
autoconf \  
automake \  
make \  
cmake  

