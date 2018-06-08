FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV PATH=$PATH:/bin/:/usr/bin/  
# Apt packages  
ADD apt_requirements.txt apt_requirements.txt  
RUN apt-get update && \  
apt-get install -y $(grep -vE "^\s*#" apt_requirements.txt | tr "\n" " ") &&\  
# CMake  
wget https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.sh && \  
chmod +x ./cmake-3.7.2-Linux-x86_64.sh &&\  
./cmake-3.7.2-Linux-x86_64.sh --skip-license && \  
# Cleanup  
rm ./cmake-3.7.2-Linux-x86_64.sh && \  
apt-get -y autoremove && apt-get -y autoclean && apt-get -y purge wget  
  
ENV CC=gcc-4.8  
ENV CXX=g++-4.8  

