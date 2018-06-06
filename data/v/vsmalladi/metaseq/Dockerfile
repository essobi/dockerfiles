# Set the base image from Miniconda  
FROM continuumio/miniconda:latest  
  
MAINTAINER Venkat Malladi <venkat.malladi@utsouthwestern.edu>  
  
  
# Install pre-requistes  
RUN apt-get -y update && \  
apt-get -y install libgl1-mesa-glx  
  
RUN \  
conda update -y conda  
  
RUN \  
conda update --all  
  
# Install metaseq version 0.5.6  
  
ENV METASEQ_VERSION=0.5.6  
RUN \  
conda install -c bioconda metaseq=${METASEQ_VERSION}  
# Finalize environment  
  
ENV PATH=$PATH:/opt/conda/bin/python  

