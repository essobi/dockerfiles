FROM ubuntu:16.04  
MAINTAINER Pulsar-Chem  
RUN apt-get update && apt-get install -y mpich \  
python3-dev \  
python3-numpy \  
libdb5.3-dev \  
cmake \  
git \  
libeigen3-dev \  
libtbb-dev  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

