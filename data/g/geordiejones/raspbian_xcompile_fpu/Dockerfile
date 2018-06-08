FROM sdthirlwall/raspberry-pi-cross-compiler  
MAINTAINER Gareth Jones <joneszone1975@gmail.com>  
  
LABEL Description="Cross compile environment for fpu on Raspbian"  
  
RUN install-debian --update wget zlib1g-dev libcurl3 ninja-build  
  
# Build and install the latest cmake  
WORKDIR /usr/src  
RUN wget https://cmake.org/files/v3.8/cmake-3.8.1.tar.gz  
RUN tar -xzf cmake-3.8.1.tar.gz  
WORKDIR /usr/src/cmake-3.8.1  
RUN /usr/src/cmake-3.8.1/bootstrap --parallel=$(nproc) --prefix=/usr && \  
make -j$(nproc) && ./bin/cmake . && make install  
  
WORKDIR /rpxc/sysroot/home  
RUN install-debian --update cups-ppdc doxygen pkg-config file  
RUN install-raspbian --update libcups2-dev libbsd-dev libusb-1.0-0-dev
libcupsimage2-dev  
  
# for come reason the following don't work so I need to install by hand in  
# build machine  
RUN install-raspbian --update libboost-program-options1.54-dev libboost-
filesystem1.54-dev libusb-dev  
  
# Set up the build environment  
ENV RPXC_IMAGE=geordiejones/raspbian_xcompile_fpu  

