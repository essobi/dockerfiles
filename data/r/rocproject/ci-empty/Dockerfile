FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
# compilers  
RUN apt-get install -y g++  
  
# tools  
RUN apt-get install -y scons  
  
# dependencies  
RUN apt-get install -y \  
libasound2-dev \  
libpulse-dev \  
libtool \  
intltool \  
autoconf \  
automake \  
make \  
cmake  

