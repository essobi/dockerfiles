FROM node:4.4.5  
MAINTAINER Taka Wang <taka@cmwang.net>  
  
## Set environment variable  
ENV DEBIAN_FRONTEND noninteractive  
  
## Install deps  
RUN apt-get update && \  
apt-get install -y libzmq3-dev && \  
npm install mocha -g

