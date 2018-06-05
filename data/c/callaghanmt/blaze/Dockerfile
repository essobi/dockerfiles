FROM ubuntu:latest  
  
MAINTAINER Martin Callaghan <m.callaghan@leeds.ac.uk>  
  
RUN apt-get -y update && apt-get install -y build-essential  
  
RUN apt-get install -y apt-utils  
  
RUN apt-get install -y gfortran  
  
RUN apt-get install -y libopenblas-base  
  
RUN apt-get install -y wget  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN mkdir /nb  
  
RUN conda install jupyter -y --quiet && mkdir /opt/notebooks  
  
RUN conda install -c blaze blaze  
  

