#  
# Builds using GCC 7.x on Bionic  
#  
FROM ubuntu:bionic  
MAINTAINER H. Birch Tree  
  
RUN apt-get -qy update && apt-get -qy install \  
git nano wget \  
cmake ninja-build \  
mingw-w64  
  
RUN groupadd coffeeusers -g 1000  
RUN useradd coffee -m -u 1000  
  
# Set up base directories for building  
USER coffee  
WORKDIR /home/coffee  
RUN mkdir -p project bridge build/bin build/libs build/out  
USER root  
  
# Set environment variables for compiler toolchain  
ENV CC=x86_64-w64-mingw32-gcc  
ENV CXX=x86_64-w64-mingw32-g++  
ENV AS=x86_64-w64-mingw32-as  
ENV LD=x86_64-w64-mingw32-ld  
  
WORKDIR /home/coffee  
USER coffee  
  
VOLUME
["/home/coffee/project","/home/coffee/build/libs","/home/coffee/build/out"]  

