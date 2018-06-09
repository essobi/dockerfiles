# Set the base image to Ubuntu  
FROM ubuntu:16.04  
# File Author / Maintainer  
MAINTAINER Matthias Becker  
  
RUN apt-get update && apt-get install -y jam openmpi-bin wget bzip2
libopenmpi-dev build-essential  
  
RUN mkdir /workdir  
WORKDIR /workdir  
RUN wget
http://alurulab.cc.gatech.edu/sites/all/projectFiles/tinge_gena/tinge-1.062.tar.bz2  
RUN tar xfj tinge-1.062.tar.bz2  
WORKDIR /workdir/TINGe-1.062  
RUN ./x-build install  
RUN mkdir /opt/tinge  
RUN cp -r bin /opt/tinge  
RUN cp -r doc /opt/tinge  

