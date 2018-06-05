#Dockerfile for cpptraj AMBER  
FROM ubuntu:latest  
  
MAINTAINER Martin Callaghan <m.callaghan@leeds.ac.uk>  
  
RUN apt-get -y update && apt-get install -y apt-utils build-essential  
  
RUN apt-get install -y gfortran  
  
RUN apt-get install -y libopenblas-base  
  
RUN apt-get install -y wget  
  
RUN apt-get install -y libblas-dev liblapacke-dev libnetcdf-dev libarpack2-dev
libboost-all-dev  
  
RUN apt-get install -y git-all  
  
RUN git clone https://github.com/Amber-MD/cpptraj.git  
  
RUN apt-get install -y libpng12-0  
  
RUN apt-get install -y libbz2-dev  
  
RUN cd cpptraj && ./configure gnu  
  
RUN cd cpptraj && make install  
  
RUN mkdir -p /nobackup  

