FROM ubuntu:latest  
MAINTAINER Patrick Kleindienst <patrick.kleindienst@web.de>  
  
ARG AURORA_VERSION=0.17.0  
ENV AURORA_CONFIG_ROOT=/home/aurora/.aurora/clusters.json  
ENV USER=aurora  
  
RUN apt-get update && \  
apt-get install -y python2.7 wget && \  
wget -c https://apache.bintray.com/aurora/ubuntu-trusty/aurora-
tools_${AURORA_VERSION}_amd64.deb && \  
dpkg -i aurora-tools_${AURORA_VERSION}_amd64.deb  
  
RUN useradd $USER \--create-home --shell /bin/bash  
  
USER aurora  
  
WORKDIR /home/aurora  

