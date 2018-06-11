FROM nvidia/cuda:8.0-devel  
  
MAINTAINER Christian Hentschel <chrstn.hntschl@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
RUN wget http://wili.cc/blog/entries/gpu-burn/gpu_burn-0.7.tar.gz && tar xzf
gpu_burn-0.7.tar.gz && make  
  
ENTRYPOINT [ "/root/gpu_burn" ]  
CMD [ "10" ] # burn for 10 secs  

