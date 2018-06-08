# Copyright (c) 2014-2018, Centre for Genomic Regulation (CRG).  
# Copyright (c) 2014-2018, Jose Espinosa-Carrasco and the respective authors.  
#  
# This file is part of Pergola.  
#  
# Pergola is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# Pergola is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with Pergola. If not, see <http://www.gnu.org/licenses/>.  
#  
############################################################  
# Dockerfile to build Pergola with all its dependencies  
# Based on ubuntu xenial  
############################################################  
  
## Set the base image to debian wheezy  
# FROM debian:wheezy  
# 7 corresponds to wheezy, this way I control the exact release  
# FROM debian:7.11  
  
## Set the base image to ubuntu xenial  
FROM ubuntu:16.04  
  
MAINTAINER Jose Espinosa-Carrasco <espinosacarrascoj@gmail.com>  
  
## Install Python and Basic Python Tools  
  
## Update always before download  
# single command save space, because each run generates a folder layer  
RUN apt-get update && \  
apt-get install -y python \  
python-dev \  
python-distribute \  
python-pip \  
gfortran \  
libblas-dev \  
liblapack-dev \  
bedtools \  
bzip2 \  
liblzma-dev \  
zlibc \  
libbz2-dev \  
zlib1g-dev \  
libhdf5-dev  
  
## Copying pergola  
COPY pergola /pergola/pergola  
COPY requirements.txt /pergola/  
COPY setup.py /pergola/  
COPY README.md /pergola/  
  
## TODO add requirements.txt file to pergola  
RUN pip install -r /pergola/requirements.txt && \  
pip install cython && \  
pip install h5py && \  
cd pergola && python setup.py install

