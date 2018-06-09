FROM ubuntu:16.04  
MAINTAINER Bruce McCleave<bruce@thinkiq.com>  
  
USER root  
  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
apt-get update && \  
apt-get install -y nodejs npm nodejs-legacy && \  
npm install forever -g && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

