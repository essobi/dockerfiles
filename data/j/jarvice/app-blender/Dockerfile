FROM nimbix/ubuntu-desktop:trusty  
MAINTAINER stephen.fox@nimbix.net  
  
ENV INSTALL_ROOT=/opt/blender  
  
RUN mkdir -p ${INSTALL_ROOT}  
WORKDIR ${INSTALL_ROOT}  
RUN apt-get update && apt-get install -y curl  
RUN curl -o blender-2.77a-linux-glibc211-x86_64.tar.bz2
http://mirror.cs.umn.edu/blender.org/release/Blender2.77/blender-2.77a-linux-
glibc211-x86_64.tar.bz2  
  
RUN tar xjf blender-2.77a-linux-glibc211-x86_64.tar.bz2 && rm -f
blender-2.77a-linux-glibc211-x86_64.tar.bz2  
  
ADD ./scripts /usr/local/scripts  
ADD ./NAE/nvidia.cfg /etc/NAE/nvidia.cfg  
  
COPY ./NAE/AppDef.json /etc/NAE/AppDef.json  
COPY ./NAE/screenshot.png /etc/NAE/screenshot.png  

