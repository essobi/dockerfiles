# versabox/installation_environment  
#  
# VersaBox  
# www.versabox.pl  
#  
# Author: Aleksander Szulc  
# Date : 09-06-2017  
#  
# Description: clean workspace for vb_robot_workspace installation  
FROM ubuntu:16.04  
# Install missing packages  
RUN apt-get update && apt-get install -y \  
jq \  
git \  
curl \  
sudo \  
lsb-release \  
python \  
python-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add user 'jenkins' to system (password: jenkins)  
RUN groupadd -g 13000 jenkins  
RUN useradd -m -s /bin/bash -u 13000 -g 13000 jenkins -G sudo  
RUN echo 'jenkins:jenkins' | chpasswd  
RUN echo 'jenkins ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
USER jenkins  
WORKDIR /home/jenkins  
ENV USER jenkins  
  
# Create .netrc file to store Bitbucket credentials  
RUN echo "machine bitbucket.org" >> /home/jenkins/.netrc  

