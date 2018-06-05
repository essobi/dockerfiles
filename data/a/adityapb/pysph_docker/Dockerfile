FROM ubuntu:14.04  
MAINTAINER user@gmail.com  
LABEL version = '0.0.1-beta'  
  
RUN apt-get update && apt-get install -yq apt-utils  
  
RUN apt-get install -yq python build-essential \  
python-dev python-numpy python-mako cython python-nose \  
mayavi2 python-qt4 git python-setuptools  
  
# For parallel support and OpenMP  
RUN apt-get install -yq libopenmpi-dev python-mpi4py python-importlib python-
unittest2 libgomp1  
  
# Some additional packages  
RUN apt-get install -yq wget curl tar gcc g++  
  
RUN export CC=gcc-4.8.4  
  
RUN apt-get install python-mock  
  
# For downloading the PySPH and setting up setup  
RUN git clone https://bitbucket.org/pysph/pysph.git  
  
RUN cd pysph && ./build_zoltan.sh /zoltan && export ZOLTAN=/zoltan && python
setup.py develop  

