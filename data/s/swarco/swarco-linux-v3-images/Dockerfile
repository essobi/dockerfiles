# -*- shell-script -*-  
FROM swarco/swarco-linux-v3-toolchain  
MAINTAINER Guido Classen <clagix@gmail.com>  
  
LABEL description="Automated Build for SWARCO Embedded Linux V3 operating
system (Rootfs/Kernel Images)"  
  
# older Docker version don't understand "ARG"  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
COPY docker_build.sh /home/builduser/  
USER builduser  
  
RUN ls -l /home/builduser  
WORKDIR /home/builduser  
RUN ./docker_build.sh  
  
#reset DEBIAN_FRONTEND to default value  
ENV DEBIAN_FRONTEND newt  
  
#USER root  

