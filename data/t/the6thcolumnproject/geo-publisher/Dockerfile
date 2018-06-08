#**************************************************************************  
# Copyright (c) 2012, The 6Th Column Project, LLC. *  
# Written by: The codewrx.org development team .et al *  
# *  
# All rights reserved. This file is part of the: *  
# The 6th Column Project, LLC / CodeWRX Software Stack *  
# *  
#**************************************************************************  
# Creates an Ubuntu 14 based image for Publisher *  
# *  
# ## . *  
# ## ## ## == *  
# ## ## ## ## === *  
# /""""""""""""""""\\___/ === *  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~ *  
# \\______ o __/ *  
# \ \ __/ *  
# \\____\\______/ *  
# *  
#**************************************************************************  
# *  
# For details, see http://6thcolumn.org/ *  
# Please also read this link *  
# http://6thcolumn.org/LICENSE *  
# *  
#**************************************************************************  
FROM ubuntu:14.04  
#tell debian based distros to forget about user input  
ENV DEBIAN_FRONTEND noninteractive  
  
#update the de distro and install some basic tools  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y curl git vim emacs  
  
#prepare the build environment  
RUN apt-get update && apt-get install -y build-essential  
  
#************* DEPENDENCIES  
#szip dependency  
RUN curl ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/szip-2.1.tar.gz | tar
xz && \  
cd szip-2.1 && \  
./configure && \  
make && \  
make install  
#hdf5 dependency  
RUN curl ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/hdf5-1.8.13.tar.gz |
tar xz && \  
cd hdf5-1.8.13 && \  
./configure && \  
make && \  
make install  
#zlib dependency  
RUN curl ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/zlib-1.2.8.tar.gz |
tar xz && \  
cd zlib-1.2.8 && \  
./configure && \  
make && \  
make install  
  
#Netcdf4-c  
RUN export CPPFLAGS=-I/hdf5-1.8.13/hdf5/include \  
LDFLAGS=-L/hdf5-1.8.13/hdf5/lib \  
LD_LIBRARY_PATH=/hdf5-1.8.13/hdf5/lib && \  
curl ftp://ftp.unidata.ucar.edu/pub/netcdf/old/netcdf-4.3.2.tar.gz | tar xz &&
\  
cd netcdf-4.3.2 && \  
./configure && \  
make && \  
make install  
  
#python & co  
RUN apt-get install -y python python-dev  
RUN curl https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install numpy  
  
#netcdf4 python  
RUN git clone https://github.com/Unidata/netcdf4-python.git && \  
cd netcdf4-python && \  
cp setup.cfg.template setup.cfg && \  
python setup.py build && \  
python setup.py install  
  
#connection to elasticseearch  
RUN pip install elasticsearch  
  
#prepare env  
ADD env /env  
  
#prepare the scripts  
ADD scripts /scripts  
  
#ENV CONTAINER_DATA /container_data  
#9200 elastic search  
#10101 container controller  

