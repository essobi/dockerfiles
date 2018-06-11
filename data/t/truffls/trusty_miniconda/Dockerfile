FROM ubuntu:trusty-20150814  
  
MAINTAINER tuky  
  
RUN apt-get update && apt-get install -y wget libglib2.0-0 libxext6 libsm6
libxrender1  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget \--quiet
https://repo.continuum.io/miniconda/Miniconda-3.10.1-Linux-x86_64.sh && \  
/bin/bash /Miniconda-3.10.1-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda-3.10.1-Linux-x86_64.sh && \  
/opt/conda/bin/conda install -y conda==3.14.1 python==2.7.9 requests==2.5.3
pyopenssl==0.15.1  
  
ENV PATH /opt/conda/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  

