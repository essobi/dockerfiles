  
FROM python:3.4  
MAINTAINER Brian Thorne <hardbyte@gmail.com>  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install deps  
RUN apt-get autoclean && apt-get update && apt-get upgrade -y  
RUN apt-get install -y -q wget curl git gcc build-essential  
RUN apt-get install -y -q libssl-dev libatlas-dev libffi-dev  
RUN apt-get install -y -q libatlas3-base libblas-dev libblas3 libatlas-base-
dev libatlas-dev  
RUN apt-get install -y -q gfortran liblapack-dev  
  
ENV LAPACK /usr/lib/liblapack.so  
ENV ATLAS /usr/lib/libatlas.so  
ENV BLAS /usr/lib/libblas.so  
  
RUN pip3 install -U pip setuptools  
RUN pip install virtualenv  

