# FaultMap  
#  
# VERSION 0.2  
FROM ubuntu:16.04  
MAINTAINER Simon Streicher <streichersj@gmail.com>  
  
# Install system level dependencies  
RUN apt-get update && apt-get install -y \  
pkg-config \  
ghostscript dvipng \  
python python-dev python-pip cython\  
git default-jdk wget \  
libfreetype6-dev libxft-dev libpng-dev libxext-dev \  
gfortran libopenblas-dev liblapack-dev \  
libhdf5-dev texlive-latex-extra  
  
# Install Miniconda  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
# Clone FaultMap repository and create environment  
RUN cd ~ && git clone https://github.com/SimonStreicher/FaultMap.git && \  
cd FaultMap && \  
export PATH=/opt/conda/bin:$PATH && \  
conda env create -f environment.yml  
  
ENV PATH /opt/conda/bin:$PATH  
  
# Use ENV to add files to PATH  
#ENV PATH /usr/local/...:$PATH  
# Default command  
CMD /bin/bash

