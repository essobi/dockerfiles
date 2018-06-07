FROM ubuntu:17.10  
  
MAINTAINER Till Salzer <till.salzer@gmail.com>  
  
ENV git_ubuntu_version 17.10  
  
LABEL description="Base Ubuntu image with git installed" \  
net.tsalzer.docker-git-ubuntu.version="${git_ubuntu_version}"  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y git  

