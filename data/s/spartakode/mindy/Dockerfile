FROM ubuntu:14.04.2  
MAINTAINER Adnan Issadeen <spartakode@outlook.com>  
  
RUN apt-get update && apt-get install wget curl unzip vim gcc bison flex
software-properties-common python-software-properties -y --force-yes  
RUN apt-add-repository ppa:git-core/ppa -y && apt-get update -y && apt-get
install git -y  
RUN mkdir /usr/src/mindy  
WORKDIR /usr/src/mindy  
RUN wget https://cmake.org/files/v3.3/cmake-3.3.2-Linux-x86_64.tar.gz && tar
-xvf cmake-3.3.2-Linux-x86_64.tar.gz && cp cmake-3.3.2-Linux-x86_64/bin/*
/usr/bin && cp -r cmake-3.3.2-Linux-x86_64/share/cmake-3.3/
/usr/share/cmake-3.3/  
RUN wget https://github.com/martine/ninja/releases/download/v1.6.0/ninja-
linux.zip && unzip ninja-linux.zip && mv ninja /usr/local/bin/  
RUN git clone https://github.com/project-mindy/mindy.git  
WORKDIR /usr/src/mindy/mindy  
RUN mkdir build && cd build && cmake .. -G Ninja && ninja && ninja test && cp
bin/mindy /bin/mindy && cp bin/mindycomp /bin/mindycomp && cp -r lib/dylan
/usr/local/lib  

