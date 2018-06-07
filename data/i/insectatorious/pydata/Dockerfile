FROM ubuntu:16.04  
  
MAINTAINER Sumanas Sarma <insectatorious+docker@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y libblas-dev checkinstall && \  
apt-get install -y libblas-doc checkinstall && \  
apt-get install -y liblapacke-dev checkinstall && \  
apt-get install -y liblapack-doc checkinstall && \  
apt-get install -y gfortran  
  
RUN apt-get install -y python3-dev python3-pip  
RUN /usr/bin/yes | pip3 install -U Cython numpy  

