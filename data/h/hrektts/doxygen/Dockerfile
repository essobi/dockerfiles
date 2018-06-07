FROM hrektts/ubuntu:16.04.20170710  
MAINTAINER mps299792458@gmail.com  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
doxygen graphviz \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
VOLUME ["/data"]  

