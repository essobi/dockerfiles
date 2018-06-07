FROM ubuntu:14.04  
MAINTAINER Traun Leyden <traun.leyden@gmail.com>  
  
# A docker container with the Nvidia kernel module and CUDA drivers installed  
  
ENV CUDA_RUN
http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_linux.run  
  
RUN apt-get update && apt-get install -q -y \  
wget \  
build-essential  
  
RUN cd /opt && \  
wget $CUDA_RUN && \  
chmod +x *.run && \  
mkdir nvidia_installers && \  
./cuda_7.0.28_linux.run -extract=`pwd`/nvidia_installers && \  
cd nvidia_installers && \  
./NVIDIA-Linux-x86_64-346.46.run -s -N --no-kernel-module  
  
RUN cd /opt/nvidia_installers && \  
./cuda-linux64-rel-7.0.28-19326674.run -noprompt  
  
# Ensure the CUDA libs and binaries are in the correct environment variables  
ENV LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-7.0/lib64  
ENV PATH=$PATH:/usr/local/cuda-7.0/bin  

