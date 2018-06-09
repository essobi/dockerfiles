#  
# Ubuntu-16.04 Docker Container  
#  
# This image can be used to build binaries that are compatible with Ubuntu
16.04  
#  
FROM ubuntu:16.04  
MAINTAINER micheli.andrea@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Dev tools  
RUN apt-get update && apt-get install -y gcc make cmake tar g++ libxml2-dev
doxygen flex bison libreadline-dev swig python-dev nano wget libboost-all-dev
libgmp-dev openjdk-8-jdk libgtest-dev lcov graphviz texlive  
  
# GTest  
RUN mkdir /tmp/gtest-build && cd /tmp/gtest-build && cmake
-DCMAKE_BUILD_TYPE=RELEASE /usr/src/gtest/ && make && mv libg* /usr/lib/ && cd
/ && rm -rf /tmp/gtest-build  
  
# Install MathSAT in /mathsat  
RUN cd /tmp && \  
wget --no-check-certificate
http://mathsat.fbk.eu/download.php?file=mathsat-5.3.13-linux-x86_64.tar.gz -O
mathsat-5.3.13-linux-x86_64.tar.gz && \  
tar xfz mathsat-5.3.13-linux-x86_64.tar.gz && \  
mv mathsat-5.3.13-linux-x86_64 /mathsat && \  
rm -rf mathsat-5.3.13-linux-x86_64.tar.gz  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
CMD /bin/bash

