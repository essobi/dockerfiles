FROM openjdk:8  
  
LABEL authors="will.rowe@stfc.ac.uk" \  
description="Docker image containing all requirements for drax pipeline"  
# Install container-wide requrements gcc, pip, zlib, libssl, make, libncurses,
fortran77, g++, R  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends \  
g++ \  
gcc \  
gfortran \  
libbz2-dev \  
libcurl4-openssl-dev \  
libgsl-dev \  
libgsl2 \  
liblzma-dev \  
libncurses5-dev \  
libpcre3-dev \  
libreadline-dev \  
libssl-dev \  
make \  
python-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install pip  
RUN curl -fsSL https://bootstrap.pypa.io/get-pip.py -o /opt/get-pip.py && \  
python /opt/get-pip.py && \  
rm /opt/get-pip.py  
# Install conda and install what we can  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget \--quiet
https://repo.continuum.io/miniconda/Miniconda3-4.3.31-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
ENV PATH /opt/conda/bin:$PATH  
RUN conda config \--add channels defaults && \  
conda config \--add channels conda-forge && \  
conda config \--add channels bioconda  
RUN curl -fsSL https://raw.githubusercontent.com/will-rowe/drax/master/drax-
conda-environment.yml -o drax-conda-environment.yml  
RUN conda install -y \--file drax-conda-environment.yml  

