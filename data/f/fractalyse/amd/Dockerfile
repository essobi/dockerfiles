FROM ubuntu:16.04  
  
MAINTAINER fractalyse <fractalyse@users.noreply.github.com>  
LABEL description="Ubuntu 16.04 with amdgpu-pro-17.40.2712.510357 for RX-550"  
  
WORKDIR /tmp  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get -y \--no-install-recommends install ca-certificates curl xz-utils \  
&& curl -L -O --referer https://support.amd.com
https://www2.ati.com/drivers/linux/beta/ubuntu/amdgpu-
pro-17.40.2712-510357.tar.xz \  
&& tar -Jxvf amdgpu-pro-17.40.2712-510357.tar.xz \  
&& rm amdgpu-pro-17.40.2712-510357.tar.xz \  
&& chmod +x ./amdgpu-pro-17.40.2712-510357/amdgpu-pro-install \  
&& ./amdgpu-pro-17.40.2712-510357/amdgpu-pro-install -y \  
&& apt-get -y install rocm-amdgpu-pro \  
&& rm -r amdgpu-pro-17.40.2712-510357 \  
&& apt-get -y remove ca-certificates curl xz-utils \  
&& apt-get -y autoremove \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log} \  
&& echo 'export LLVM_BIN=/opt/amdgpu-pro/bin' | tee /etc/profile.d/amdgpu-
pro.sh  
  
ENV GPU_FORCE_64BIT_PTR=0  
ENV GPU_MAX_HEAP_SIZE=100  
ENV GPU_USE_SYNC_OBJECTS=1  
ENV GPU_MAX_ALLOC_PERCENT=100  
ENV GPU_SINGLE_ALLOC_PERCENT=100  
  
CMD ["/bin/bash"]  

