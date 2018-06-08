FROM ubuntu:xenial  
MAINTAINER Stefan Kaestle <stefan.kaestle@inf.ethz.ch>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python-networkx python-pygraphviz libgv-python python-numpy python-pygraph
python-matplotlib \  
wget net-tools \  
texlive-full \  
build-essential \  
libnuma-dev \  
git \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  

