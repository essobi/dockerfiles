############################################################  
# Dockerfile to build container images for single cell  
# kallisto fork including sratools  
# Based on ubuntu 16.04  
############################################################  
  
FROM ubuntu:16.04  
  
# File Author / Maintainer  
MAINTAINER Matthias Becker <mbecker@uni-bonn.de>  
  
# install dependencies first  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
cmake \  
hdf5-tools \  
libhdf5-dev \  
hdf5-helpers \  
libhdf5-serial-dev \  
libssh2-1-dev \  
libcurl4-openssl-dev \  
icu-devtools \  
libssl-dev \  
libxml2-dev \  
git \  
apt-utils \  
pigz  
  
# install sra-toolkit  
WORKDIR /docker  
RUN wget "https://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/2.8.2-1/sratoolkit.2.8.2-1-ubuntu64.tar.gz" &&
\  
tar zxfv sratoolkit.2.8.2-1-ubuntu64.tar.gz  
RUN cp -r sratoolkit.2.8.2-1-ubuntu64/bin/* /usr/bin  
  
# install kallisto from source  
WORKDIR /docker  
RUN git clone https://github.com/makaho/kallisto.git  
WORKDIR /docker/kallisto  
RUN mkdir build  
WORKDIR /docker/kallisto/build  
RUN cmake .. && \  
make && \  
make install  

