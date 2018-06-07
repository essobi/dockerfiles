FROM centos:7  
ENV ISPC_VERSION="1.9.1"  
ENV EMBREE_VERSION="2.16.4"  
RUN mkdir /gitlab  
ENV HOME=/gitlab  
  
# All builds will be done in home dir  
WORKDIR $HOME  
  
# Install all req packages  
RUN yum install -y wget git make cmake.x86_64 gcc gcc-c++ tbb.x86_64 tbb-
devel.x86_64 libXcursor.x86_64 libXcursor-devel.x86_64 libXrandr.x86_64
libXrandr-devel.x86_64 libXinerama.x86_64 libXinerama-devel.x86_64 mesa-libGL-
devel  
  
# Download and install embree  
RUN wget
https://github.com/embree/embree/releases/download/v${EMBREE_VERSION}/embree-${EMBREE_VERSION}.x86_64.rpm.tar.gz
&& tar -xvf embree-${EMBREE_VERSION}.x86_64.rpm.tar.gz && rpm -iv embree-
devel-${EMBREE_VERSION}-1.x86_64.rpm embree-lib-${EMBREE_VERSION}-1.x86_64.rpm
--force && rm embree-${EMBREE_VERSION}.x86_64.rpm.tar.gz *.rpm  
  
# Download and unpack ISPC  
RUN wget
https://downloads.sourceforge.net/project/ispcmirror/v${ISPC_VERSION}/ispc-v${ISPC_VERSION}-linux.tar.gz
&& tar -xvf ispc-v${ISPC_VERSION}-linux.tar.gz && rm
ispc-v${ISPC_VERSION}-linux.tar.gz  
ENV PATH $PATH:$HOME/ispc-v${ISPC_VERSION}-linux  
  
CMD ["/bin/bash -l"]  

