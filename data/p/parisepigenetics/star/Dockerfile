###########################################################  
# Dockerfile to build star container images  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:latest  
  
# File Author / Maintainer  
MAINTAINER Costas Bouyioukos <costas.bouyioukos@univ-paris-diderot.fr>  
  
# Update the repository sources list  
RUN apt-get update  
RUN apt-get upgrade --yes  
  
# Install compiler, git etc.  
RUN apt-get install --yes \  
build-essential \  
gcc-multilib \  
zlib1g-dev \  
git  
  
RUN apt-get autoclean  
RUN apt-get autoremove --yes  
  
# Install STAR  
WORKDIR /usr/local/  
RUN git clone https://github.com/alexdobin/STAR.git  
WORKDIR /usr/local/STAR/  
RUN git checkout 2.5.3a  
WORKDIR /usr/local/STAR/source  
RUN make LDFLAGSextra=-flto CXXFLAGSextra="-flto -march=native"  
ENV PATH /usr/local/STAR/source:$PATH  

