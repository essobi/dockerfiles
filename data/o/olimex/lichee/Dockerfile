FROM ubuntu:12.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
build-essential \  
g++-multilib \  
lib32z1 \  
uboot-mkimage \  
&& rm -rf /var/lib/apt/lists/*  

