FROM ubuntu:artful  
MAINTAINER tinou98  
  
RUN dpkg --add-architecture i386  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y build-essential python wget zip git  
RUN apt-get install -y gcc-mingw-w64 gcc gcc-multilib g++ g++-multilib  
RUN apt-get install -y make cmake doxygen debhelper  
  
RUN apt-get install -y libgl1-mesa-dev libx11-dev libxcursor-dev libxi-dev
libxinerama-dev libxrandr-dev libxxf86vm-dev  
RUN apt-get install -y libgl1-mesa-dev:i386 libx11-dev:i386 libxcursor-
dev:i386 libxinerama-dev:i386 libxrandr-dev:i386 libxxf86vm-dev:i386  
RUN apt-get install -y pkg-config  
  
ENV ARCH linux64  
ENV BUILD_TYPE Release  
  
WORKDIR /workdir  

