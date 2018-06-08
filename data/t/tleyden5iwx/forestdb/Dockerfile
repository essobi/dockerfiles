  
FROM centos:centos7  
  
MAINTAINER Traun Leyden <tleyden@couchbase.com>  
  
# forestdb installs here, so add to linker PATH  
ENV LD_LIBRARY_PATH /usr/local/lib/  
# Install yum dependencies  
RUN yum -y update && \  
yum groupinstall -y development && \  
yum install -y \  
cmake \  
git \  
snappy-devel \  
sudo \  
tar \  
wget  
  
# ForestDB  
RUN cd /root && \  
git clone git://github.com/couchbase/forestdb && \  
cd forestdb && \  
mkdir build && \  
cd build && \  
cmake ../ && \  
make all && \  
make install  
  

