FROM ubuntu:trusty  
MAINTAINER Ricardo Amaro <ricardo.amaro_at_acquia.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list; \  
apt-get update; \  
apt-get -y upgrade; \  
apt-get -y install build-essential software-properties-common unzip vim-tiny
git curl wget htop mc; \  
apt-get clean; \  
apt-get autoclean; \  
apt-get -y autoremove;  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["/bin/bash"]  

