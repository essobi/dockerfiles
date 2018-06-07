# Version 0.0.1  
FROM ubuntu:12.04  
  
MAINTAINER HuBo <hubo@21cn.com>  
  
RUN rm -fr /bin/sh && ln -s /bin/bash /bin/sh && apt-get update  
  
RUN apt-get -y install python bc  
  
RUN apt-get -y install git gnupg flex bison gperf build-essential \  
zip curl libc6-dev libncurses5-dev x11proto-core-dev \  
libx11-dev libreadline6-dev libgl1-mesa-glx \  
libgl1-mesa-dev g++-multilib mingw32 tofrodos \  
python-markdown libxml2-utils xsltproc zlib1g-dev \  
xsltproc uboot-mkimage gettext ia32-libs lib32ncurses5-dev \  
libtool autoconf gcc-4.4 g++-4.4 g++-4.4-multilib gcc-4.4-multilib  
  
RUN ln -s /usr/lib/i386-linux-gnu/mesa/libGL.so.1 /usr/lib/i386-linux-
gnu/libGL.so && \  
rm /usr/bin/gcc && \  
ln -s /usr/bin/gcc-4.4 /usr/bin/gcc && \  
rm /usr/bin/g++ && \  
ln -s /usr/bin/g++-4.4 /usr/bin/g++  
  
RUN apt-get -y install openjdk-7-jdk  
  
RUN echo "* - nofile 8192" >> /etc/security/limits.conf  
  
RUN echo "umask 022" >> /etc/profile  
  
RUN mkdir /source  
  
WORKDIR /source  
  
  

