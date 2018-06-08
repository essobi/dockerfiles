FROM debian:9.4  
  
MAINTAINER Ghifari160 <ghifari160@ghifari160.com>  
  
# Disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update Debian  
RUN apt update && apt upgrade -y --autoremove && \  
apt clean && rm -rf /var/lib/apt/lists/*  
# Install some utilities  
RUN apt update && \  
apt install -y software-properties-common \  
nano wget && \  
apt clean && rm -rf /var/lib/apt/lists/*  

