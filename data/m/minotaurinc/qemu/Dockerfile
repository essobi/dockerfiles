FROM ubuntu:16.04  
MAINTAINER Derek Straka <derek@asterius.io>  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV USER root  
  
# build depends  
RUN apt-get update && \  
apt-get --quiet --yes install \  
build-essential pkg-config curl wget \  
software-properties-common gcc-multilib \  
libglib2.0-dev zlib1g-dev \  
dh-autoreconf bison flex && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*  
  
RUN curl http://wiki.qemu-project.org/download/qemu-2.7.0-rc1.tar.bz2 -sSf >
qemu-2.7.0-rc1.tar.bz2 && \  
tar -jxf qemu-2.7.0-rc1.tar.bz2 && \  
cd qemu-2.7.0-rc1 && \  
mkdir build && cd build && \  
../configure --target-list=arm-softmmu,arm-linux-user,x86_64-linux-
user,x86_64-softmmu && \  
make -j 12 && make install && \  
cd ../ && rm -rf qemu-*  
  
RUN mkdir /qemu  
VOLUME ["/qemu"]  
WORKDIR /qemu  
CMD ["/bin/bash"]  

