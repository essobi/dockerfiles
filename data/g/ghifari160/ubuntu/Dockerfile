FROM ubuntu:16.04  
  
MAINTAINER Ghifari160 <ghifari160@ghifari160.com>  
  
# Disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update Ubuntu  
RUN apt update && apt upgrade -y --autoremove && \  
apt clean && rm -rf /var/lib/apt/lists/*  
# Install some utilities  
RUN apt update && \  
apt install -y software-properties-common \  
language-pack-en-base nano wget && \  
apt clean && rm -rf /var/lib/apt/lists/*  

