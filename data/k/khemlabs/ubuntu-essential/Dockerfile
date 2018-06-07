############################################################  
# Dockerfile to build Ubuntu Images  
# Based on Ubuntu 14.04  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:trusty  
  
# File Author / Maintainer  
MAINTAINER Maintaner khemlabs  
  
  
# Update the repository and install tools  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
vim \  
wget \  
build-essential \  
nfs-common \  
inotify-tools  

