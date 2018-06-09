## docker-lime-build-kernel-module  
FROM debian:jessie  
MAINTAINER Andrew Krug <andrewkrug@gmail.com>  
  
RUN apt-get update -y  
RUN DEBIAN_FRONTEND=noninteractive  
RUN apt-get install -y -qq gcc g++ wget git make dpkg-dev  
  
RUN mkdir -p /usr/src/kernels  
  
WORKDIR /usr/src/kernels  
  
RUN git clone https://github.com/504ensicsLabs/LiME  
  
WORKDIR /usr/src/kernels/linux  
  
WORKDIR /usr/src/kernels/LiME/src  
  
RUN apt-get install linux-headers-*generic* -qq -y  
RUN mkdir /opt/limemodules  
# From here you would pull down your kernel source and build it relative to
the linux kernel source tree prepared in /usr/src/kernels/linux  
VOLUME ["/opt/limemodules/"]  
  
CMD for KERNS in /lib/modules/*; do make -C $KERNS/build
M=/usr/src/kernels/LiME/src && current="`echo $KERNS | cut -d '/' -f4`" && mv
lime.ko /opt/limemodules/$current.ko && echo $current; done  

