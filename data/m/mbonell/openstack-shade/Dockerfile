# Dockerfile for building a development environment to work with the  
# OpenStack Python SDK Shade to create cloud native apps.  
FROM ubuntu:16.04  
MAINTAINER Marcela Bonell <marcelabonell@gmail.com>  
  
# Update the repository sources list and install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
libssl-dev \  
libffi-dev \  
python-dev \  
libxml2-dev \  
libxslt1-dev \  
python-pip \  
vim \  
git \  
wget  
  
# Install Shade  
RUN pip install shade  
  
WORKDIR /root  
  
# Create the config file to work with the clouds  
RUN wget https://raw.githubusercontent.com/MBonell/openstack-sdks-
challenges/master/shade/clouds.yml && \  
mkdir -p .config/openstack && \  
mv clouds.yml .config/openstack  

