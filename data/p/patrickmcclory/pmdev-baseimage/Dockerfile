# Docker image for managing audio and video files for podcasting  
#  
# Includes AWS Cli tools and updated apt-get repo with PPA for ffmpeg  
# as well as installs of SoX and ffmpeg  
#  
# Currently installs: awscli 1.7.23  
FROM ubuntu:14.10  
MAINTAINER Patrick McClory <pmcclory@gmail.com>  
  
RUN \  
sudo apt-get update -y -qq && \  
sudo apt-get install software-properties-common wget python-pip git-core -y
-qq && \  
sudo pip install awscli==1.7.23  
  
ENV HOME /root  
  
WORKDIR /root  
  
CMD ["bash"]  

