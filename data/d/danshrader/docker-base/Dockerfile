FROM ubuntu:16.04  
# https://github.com/beevelop/docker-nodejs/blob/master/Dockerfile  
ENV NODEJS_VERSION=8.9.3 \  
PATH=$PATH:/opt/node/bin  
  
WORKDIR "/opt/node"  
  
# Install Stuff I need.  
RUN apt-get update  
RUN apt-get install -y wget  
RUN wget
https://github.com/spf13/hugo/releases/download/v0.33/hugo_0.33_Linux-64bit.deb  
RUN dpkg -i hugo*.deb  
RUN apt-get install -y curl  
RUN curl -sL
https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz
| tar xz --strip-components=1  
RUN rm -rf /var/lib/apt/lists/*  
RUN npm install -g firebase-tools

