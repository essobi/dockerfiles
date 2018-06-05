############################################################  
# Dockerfile to build container images for Drop-seq pipeline  
# including STAR aligner  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Kathrin Klee <klee@uni-bonn.de>  
  
# Update the repository sources list  
RUN apt-get update && apt-get install -y openjdk-7-jre-headless && apt-get
install -y wget && apt-get install -y unzip  
  
# Install compiler and perl stuff  
RUN apt-get install --yes \  
build-essential \  
gcc-multilib \  
apt-utils \  
zlib1g-dev \  
vim-common  
  
# Install git  
RUN apt-get install -y git  
  
# Install STAR  
WORKDIR /usr/local/  
RUN pwd  
RUN git clone https://github.com/alexdobin/STAR.git  
WORKDIR /usr/local/STAR/  
RUN pwd  
RUN git checkout 2.5.1b  
WORKDIR /usr/local/STAR  
RUN pwd  
RUN make STAR  
ENV PATH /usr/local/STAR/source:$PATH  
  
# Install Drop-seq-tools  
WORKDIR /usr/local/Drop-seq_tools  
RUN wget "http://mccarrolllab.com/download/922/Drop-seq_tools-1.12.zip" && \  
unzip Drop-seq_tools-1.12.zip  

