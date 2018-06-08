FROM phusion/baseimage:0.9.18  
MAINTAINER hazim1093 <hazim_malik@hotmail.com>  
  
# Install build essential for `make`  
RUN apt-get update && apt-get install -y wget jq git perl unzip build-
essential  
  
# Install packer  
ENV PACKER_VERSION 0.10.1  
RUN mkdir -p /opt/packer  
RUN wget -nc -q
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
-P /opt/packer  
RUN unzip -q /opt/packer/packer_${PACKER_VERSION}_linux_amd64.zip -d
/opt/packer  
ENV PATH $PATH:/opt/packer  
  
# Make directory which will contain the packer project and expose as volume  
RUN mkdir -p /usr/src/app  
VOLUME /usr/src/app  
  
# Change working directory  
WORKDIR /usr/src/app  

