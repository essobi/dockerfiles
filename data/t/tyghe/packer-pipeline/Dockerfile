# Docker image for packer stuff  
#  
# docker build --rm=true -t tyghe/packer-pipeline  
  
FROM jmccann/drone-chefdk  
MAINTAINER Tyghe Vallard <vallardt@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y python python-pip unzip && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sSL
https://releases.hashicorp.com/packer/0.10.1/packer_0.10.1_linux_amd64.zip >
packer.zip && \  
unzip packer.zip && \  
mv packer /usr/local/bin/packer  

