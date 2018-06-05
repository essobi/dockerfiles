FROM ubuntu:latest  
  
MAINTAINER "Gaurav Kaushik" <gaurav@sevenbridges.com>  
  
# Update and install necessary tools  
RUN apt-get update -y  
RUN apt-get install -y \  
build-essential \  
cmake \  
python \  
python-pip \  
python-dev \  
hdf5-tools \  
libhdf5-dev \  
hdf5-helpers \  
libhdf5-serial-dev \  
git \  
apt-utils \  
vim  
  
# Add Kallisto to container and give proper permissions  
RUN mkdir /opt/kallisto  
COPY kallisto_linux-v0.43.0/ /opt/kallisto/  
RUN chmod a+x /opt/kallisto  
ENV PATH /opt/kallisto:$PATH  
  
# Open container in bash terminal  
CMD ["/bin/bash"]

