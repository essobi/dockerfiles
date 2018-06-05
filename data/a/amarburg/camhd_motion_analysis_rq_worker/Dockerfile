#  
FROM ubuntu:xenial  
MAINTAINER Aaron Marburg <amarburg@apl.washington.edu>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update && apt-get install --no-install-recommends --yes libcurlpp-
dev libcurl4-openssl-dev \  
libopencv-dev rake g++ cmake git \  
libboost-filesystem-dev libeigen3-dev libceres-dev \  
bzip2 ca-certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
libtclap-dev mercurial subversion wget  
  
## Use miniconda instead of system Python  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.3.14-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
ENV PATH /opt/conda/bin:$PATH  
  
RUN conda install setuptools wheel pillow redis numpy dask cytoolz numpy  
RUN pip install conan rq py-cpuinfo  
  
## Resolve a bug in the current xenial (and yakkety?) package for Ceres  
RUN touch /usr/include/ceres/internal/config.h  
  
## Resolve a bug in the current xenial (and yakkety?) package for curlpp  
RUN sed -i s/std::string\\(\\\\\\([a-zA-Z\ \\\\\"]*\\\\\\)\\)/\\\\\1/
/usr/include/curlpp/Option.inl  
  
## Install pycamhd  
WORKDIR /code  
RUN git clone https://github.com/CamHD-Analysis/pycamhd-lazycache.git  
WORKDIR /code/pycamhd-lazycache  
RUN pip install .  

