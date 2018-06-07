# Start with Ubuntu base image  
FROM buildpack-deps:trusty  
MAINTAINER Halo9Pan <halo9pan@gmail.com>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
linux-headers-generic linux-image-generic \  
build-essential bash-completion wget  
  
# CUDA version - as the kernel is shared the host and container must
correspond  
ENV NVIDIA_VERSION=352.63  
# Install NVIDIA driver (silent, no kernel)  
RUN cd /tmp &&\  
wget -q
http://http.download.nvidia.com/XFree86/Linux-x86_64/${NVIDIA_VERSION}/NVIDIA-
Linux-x86_64-${NVIDIA_VERSION}.run && \  
chmod +x NVIDIA-Linux-x86_64-*.run && ./NVIDIA-Linux-x86_64-*.run -s --no-
kernel-module && \  
rm -rf *  

