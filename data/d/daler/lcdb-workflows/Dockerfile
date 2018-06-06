FROM ubuntu:14.04  
MAINTAINER Ryan Dale <dalerr@niddk.nih.gov>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
bzip2 \  
ca-certificates \  
git \  
libglib2.0-0 \  
libsm6 \  
libxext6 \  
libxtst6 \  
libxrender1 \  
mysql-client \  
wget \  
x11-apps \  
zlib1g-dev  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --no-check-certificate --quiet
https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \  
/bin/bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda3-latest-Linux-x86_64.sh  
  
ENV PATH /opt/conda/bin:$PATH  
RUN mkdir /opt/lcdb  
COPY requirements.txt /tmp/  
RUN conda install -y -c bioconda -c r --file /tmp/requirements.txt  
ENV DISPLAY :0  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
ENV USER=lcdb  
WORKDIR /opt/lcdb  

