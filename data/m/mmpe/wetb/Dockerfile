# Docker file for gitlab CI test image  
FROM buildpack-deps:jessie  
  
MAINTAINER Mads M. Pedersen <mmpe@dtu.dk>  
  
ENV SHELL /bin/bash  
  
RUN apt-get update \  
&& apt-get install --fix-missing -y -q \  
git-all \  
python3-pip \  
python3-dev \  
cython3 \  
build-essential \  
python3-numpy \  
python3-matplotlib \  
python3-scipy \  
locales \  
python3-xlrd \  
python3-h5py \  
python3-tables \  
python3-pandas \  
&& apt-get autoremove -y \  
&& apt-get clean -y  
  
ENV LANG C.UTF-8  
#RUN locale-gen C.UTF-8  
#RUN dpkg-reconfigure locales  
#RUN apt-get install -y libhdf5-dev  
RUN pip3 install -U setuptools  
RUN pip3 install paramiko  
RUN pip3 install sshtunnel  
RUN pip3 install psutil  
RUN pip3 install pytest-cov  
RUN git clone https://gitlab.windenergy.dtu.dk/toolbox/WindEnergyToolbox.git  
RUN pip3 install -e ./WindEnergyToolbox  
  

