FROM ubuntu:trusty  
MAINTAINER Mike Henders <mike.henders@gmail.com>  
  
# Prevent dpkg errors  
ENV TERM=xterm-256color  
  
# Install node.js  
RUN apt-get update && \  
apt-get install curl -y && \  
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - && \  
apt-get install -y nodejs  
  
COPY . /app  
WORKDIR /app  
  
# Install application dependencies  
RUN npm install -g mocha && \  
npm install  
  
# Set mocha test runner as the entry point  
ENTRYPOINT ["mocha"]  

