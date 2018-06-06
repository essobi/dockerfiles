# Start with Ubuntu base image  
FROM ubuntu:14.04  
MAINTAINER Chintak Sheth <chintaksheth@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CUDA_MAJOR 7_0  
ENV CUDA_VERSION 7.0.28  
# Change to the /tmp directory  
RUN cd /tmp && \  
# Download run file  
wget
http://developer.download.nvidia.com/compute/cuda/$CUDA_MAJOR/Prod/local_installers/cuda_${CUDA_VERSION}_linux.run
&& \  
# Make the run file executable and extract  
chmod +x cuda_*_linux.run && ./cuda_*_linux.run -extract=`pwd` && \  
# Install CUDA drivers (silent, no kernel)  
./NVIDIA-Linux-x86_64-*.run -s --no-kernel-module && \  
# Install toolkit (silent)  
./cuda-linux64-rel-*.run -noprompt && \  
# Clean up  
rm -rf *  
  
# Add to path  
ENV CUDA_HOME=/usr/local/cuda  
RUN echo "export CUDA_HOME=/usr/local/cuda" >> /root/.bashrc \  
&& echo "export PATH=${CUDA_HOME}/bin:$PATH" >> /root/.bashrc \  
&& echo "LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH" >> /root/.bashrc  
  
WORKDIR /tmp/  
ADD cudnn-7.0-linux-x64-v3.0-prod.tgz .  
RUN cp cuda/include/cudnn.h ${CUDA_HOME}/include/ && \  
cp cud*/libcudnn_static.a ${CUDA_HOME}/lib64/ && \  
cp cuda/lib64/libcudnn.so.7.0.64 ${CUDA_HOME}/lib64/ && \  
ln -s ${CUDA_HOME}/lib64/libcudnn.so.7.0.64 ${CUDA_HOME}/lib64/libcudnn.so.7.0
&& \  
ln -s ${CUDA_HOME}/lib64/libcudnn.so.7.0 ${CUDA_HOME}/lib64/libcudnn.so && \  
rm -r cuda  

