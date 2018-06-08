FROM nvidia/cuda:8.0-devel-ubuntu16.04  
  
MAINTAINER fractalyse <fractalyse@users.noreply.github.com>  
LABEL description="Ubuntu 16.04 with latest nvidia-drivers and amdgpu-pro"  
  
WORKDIR /tmp  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get -y autoremove \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
ENV GPU_FORCE_64BIT_PTR=0  
ENV GPU_MAX_HEAP_SIZE=100  
ENV GPU_USE_SYNC_OBJECTS=1  
ENV GPU_MAX_ALLOC_PERCENT=100  
ENV GPU_SINGLE_ALLOC_PERCENT=100  
  
CMD ["/bin/bash"]  

