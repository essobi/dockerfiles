# FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04  
FROM ubuntu:16.04  
# ========== Anaconda for Python3 ==========  
# https://hub.docker.com/r/continuumio/anaconda3/~/dockerfile/  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion dbus  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
# Install basic dependencies  
RUN apt-get install -y cmake build-essential pkg-config libpython3-dev \  
libboost-python-dev libboost-dev python3 zlib1g-dev  
  
# ======== configure python environment ========  
WORKDIR /root/code/  
  
# The environmental file for parameterized is in soccerrl  
RUN git clone https://github.com/dwicke/soccerRL.git soccerrl  
  
WORKDIR /root/code/soccerrl/  
RUN conda create -y -n parameterized  
# ENV PYTHONPATH /root/code/parameterized:$PYTHONPATH  
ENV PATH /opt/conda/envs/parameterized/bin:$PATH  
RUN echo "source activate parameterized" >> /root/.bashrc  
RUN conda env update -f environment.yml  
  
# Need this to pass the last check in config.py.  
# Otherwise, the process is exiting.  
ENV CIRCLECI=true  
  
ENV BASH_ENV /root/.bashrc  
  
# ========== Install HFO in parameterized env ==========  
RUN apt-get install qt4-dev-tools -y  
  
RUN apt-get install -y libboost-filesystem-dev libboost-system-dev flex  
  
WORKDIR /root/code/  
RUN git clone https://github.com/LARG/HFO.git && \  
cd HFO && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_BUILD_TYPE=RelwithDebInfo ..  
  
WORKDIR /root/code/HFO/build  
RUN make -j4  
RUN make install  
  
WORKDIR /root/code/HFO  
RUN pip install .  
  
WORKDIR /root/code/  
# Use changed code  
RUN git clone https://github.com/dwicke/gym-soccer.git  
  
RUN cd gym-soccer && \  
pip install -e .  
  
## Need this in order for gym-soccer to work  
RUN conda install libgcc  
  
## install pytorch numpy scipy  
# RUN conda install pytorch torchvision -c soumith  
# RUN conda install -c anaconda numpy  
# RUN conda install -c anaconda scipy  

