FROM nvidia/cuda:9.0-runtime-ubuntu16.04  
MAINTAINER John Goodwin <john@jjgoodwin.com>  
  
WORKDIR /root  
  
# Env setup  
ENV ETH_VER=0.12.0  
ENV GPU_FORCE_64BIT_PTR=0  
ENV GPU_MAX_HEAP_SIZE=100  
ENV GPU_USE_SYNC_OBJECTS=1  
ENV GPU_MAX_ALLOC_PERCENT=100  
ENV GPU_SINGLE_ALLOC_PERCENT=100  
ENV ETH_DOWNLOAD_URL=https://github.com/ethereum-
mining/ethminer/releases/download/v$ETH_VER/ethminer-$ETH_VER-Linux.tar.gz  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -fsSL "$ETH_DOWNLOAD_URL" -o ethminer.tar.gz \  
&& tar -C /usr/local -xzf ethminer.tar.gz \  
&& rm ethminer.tar.gz  
  
ENTRYPOINT ["/usr/local/bin/ethminer", "-U"]  

