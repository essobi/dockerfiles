FROM fedora:latest  
  
# compilers  
RUN dnf install -y gcc-c++  
  
# tools  
RUN dnf install -y \  
pkgconfig \  
scons \  
gengetopt \  
doxygen \  
graphviz  
  
# dependencies  
RUN dnf install -y \  
libuv-devel \  
sox-devel \  
make \  
cmake  

