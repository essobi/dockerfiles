FROM abuisine/nvidia:375.66-7  
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>"
version="0.3.4b-nvidia-7"  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \  
&& apt-get install -yqq --no-install-recommends \  
vim-tiny \  
flip \  
libcurl3 \  
curl \  
&& apt-get -yqq clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV EWBF_VERSION=0.3.4b  
  
WORKDIR /home/ewbf  
RUN curl -Lks https://github.com/nanopool/ewbf-
miner/releases/download/v${EWBF_VERSION}/Zec.miner.${EWBF_VERSION}.Linux.Bin.tar.gz
| tar zxvf -  
ENV GPU_FORCE_64BIT_PTR=0 GPU_MAX_HEAP_SIZE=100 GPU_USE_SYNC_OBJECTS=1
GPU_MAX_ALLOC_PERCENT=100 GPU_SINGLE_ALLOC_PERCENT=100  
COPY resources/EWBF.py /usr/local/bin/  
  
ENV WALLET_ADDRESS="t1cneddNodVxpPoSEm1hHyCyCoT7uwUNqzz" \  
HOSTS="eu1-zcash.flypool.org:3333:x"  
CMD [ "--collector-port", "9090", "--miner-module", "EWBF", "--miner-port",
"42000" ]  
#HOSTS should be setted as follows: <hostname>:<port>:<password>

