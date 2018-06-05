FROM continuumio/miniconda  
MAINTAINER Birdhouse <wps@dkrz.de>  
  
LABEL Description="Birdhouse base image" Vendor="Birdhouse" Version="0.2.4"  
# Install common debian packages  
RUN apt-get update -y && apt-get install -y sudo wget curl build-essential
unzip  
  
# add conda channels  
RUN conda config \--set channel_priority true && \  
conda config \--add channels defaults && \  
conda config \--append channels birdhouse  
  
# Install conda packages  
RUN conda update -y conda && conda install -y python=2.7 openssl curl mako  

