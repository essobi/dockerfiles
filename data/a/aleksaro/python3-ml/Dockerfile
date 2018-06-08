#  
# python3-ml: Sets up a boilerplate Docker environment for machine learning
with  
# NVIDIA CUDA and Python 3.  
#  
# Base image is python-base  
FROM aleksaro/python3-base:9.0-cudnn7-ubuntu16.04  
LABEL maintainer "Aleksander Rognhaugen"  
  
# Install development files for HDF5  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libhdf5-dev  
  
# Cleanup apt-get  
RUN apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Install general-purpose libraries useful for machine learning in Python  
RUN pip3 install \  
h5py \  
PyYAML \  
pandas \  
scikit-learn  
  
# Install TensorFlow  
RUN pip3 install --upgrade tensorflow-gpu  
  
# Set default working directory and image startup command  
WORKDIR "/root"  
CMD ["/bin/bash"]  

