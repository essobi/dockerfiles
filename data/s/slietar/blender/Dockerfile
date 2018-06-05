FROM ubuntu:17.10  
MAINTAINER Simon Liétar <sim.lietar@outlook.com>  
  
RUN mkdir -p /tmp/blender_install /tmp/bin  
RUN apt-get -qq update && apt-get -qq upgrade  
RUN apt-get -qq install bzip2 libfontconfig1 libfreetype6 libglu1-mesa
libsdl1.2debian libxi6 libxrender1 wget  
RUN wget -q -O /tmp/blender.tar.bz2
http://mirror.cs.umn.edu/blender.org/release/Blender2.78/blender-2.78c-linux-
glibc219-x86_64.tar.bz2  
RUN tar -xjf /tmp/blender.tar.bz2 -C /tmp/blender_install  
RUN cp /tmp/blender_install/*/blender /tmp/bin/blender  
ENV PATH="/tmp/bin:${PATH}"  
RUN mkdir -p /app  
WORKDIR /app  

