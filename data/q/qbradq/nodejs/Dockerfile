# Image configuration  
FROM ubuntu:rolling  
MAINTAINER qbradq@gmail.com  
  
# Base packages  
RUN apt-get -qq update && apt-get -qq install \  
curl \  
tar \  
xz-utils  
  
# Node installation  
RUN \  
curl https://nodejs.org/dist/v8.3.0/node-v8.3.0-linux-x64.tar.xz | \  
tar -xJ --strip-components=1 -C /usr/local  

