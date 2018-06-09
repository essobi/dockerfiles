FROM debian:jessie  
MAINTAINER Taotao Hsu <taotaohsu@gmail.com>  
  
RUN \  
apt-get update && \  
apt-get install -y \  
build-essential \  
curl \  
&& \  
rm -rf /var/lib/apt/lists/* && \  
curl https://sh.rustup.rs -sSf | sh -s -- -v -y  
  
ENV PATH="${PATH}:/root/.cargo/bin"  
  
CMD ["/bin/bash"]  

