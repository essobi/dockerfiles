FROM jupyter/scipy-notebook  
# Adds Libpostal + Python binaries to Jupyter's SciPy Notebook  
LABEL maintainer='David Riordan <dr@daveriordan.com>'  
  
USER root  
  
# LIBPOSTAL  
# Install Libpostal dependencies  
RUN apt-get update &&\  
apt-get install -y \  
git \  
make \  
curl \  
autoconf \  
automake \  
libtool \  
pkg-config  
  
# Download libpostal source to /usr/local/libpostal  
RUN cd /usr/local && \  
git clone https://github.com/openvenues/libpostal  
  
# Create Libpostal data directory at /var/libpostal/data  
RUN cd /var && \  
mkdir libpostal && \  
cd libpostal && \  
mkdir data  
  
# Install Libpostal from source  
RUN cd /usr/local/libpostal && \  
./bootstrap.sh && \  
./configure --datadir=/var/libpostal/data && \  
make -j4 && \  
make install && \  
ldconfig  
  
# Install Libpostal python Bindings  
USER $NB_USER  
RUN pip install \  
postal  

