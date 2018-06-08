FROM ubuntu:trusty  
MAINTAINER Scott Crooks <scott.crooks@gmail.com>  
  
# Prevent dpkg errors  
ENV TERM=xterm-256color  
  
# Set mirrors to PDX  
RUN sed -i "s/archive.ubuntu.com/mirror.pnl.gov/g" /etc/apt/sources.list  
  
# Install node.js  
RUN apt-get update && \  
apt-get install curl -y && \  
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \  
apt-get install -y nodejs  
  
COPY . /app  
WORKDIR /app  
  
# Install application dependencies  
RUN npm install -g mocha && \  
npm install  
  
# Set mocha test runner as entrypoint  
ENTRYPOINT ["mocha"]  

