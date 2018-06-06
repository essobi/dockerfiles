FROM ubuntu:14.04  
  
RUN apt-get update -qq && \  
apt-get install -y nodejs npm && \  
npm install -g coffee-script && \  
ln -s /usr/bin/nodejs /usr/bin/node  
# simple tests  
RUN node \--version | grep v0.10.25 && \  
npm --version | grep 1.3.10 && \  
coffee --version | grep 1.7.1  

