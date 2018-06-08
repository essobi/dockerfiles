FROM debian:jessie  
MAINTAINER Silvan Wegmann <swegmann@narf.ch>  
  
ENV USER root  
ENV PATH $PATH:/root/.cargo/bin  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
file \  
build-essential \  
nasm \  
grub-common \  
grub-pc-bin \  
xorriso \  
curl \  
git && \  
curl https://sh.rustup.rs -sSf | sh -s -- -y && \  
export PATH=$PATH:/root/.cargo/bin && \  
rustup update nightly-2016-05-26 && \  
rustup override add nightly-2016-05-26  
  
VOLUME ["/source"]  
WORKDIR /source  
CMD ["/bin/bash"]  

