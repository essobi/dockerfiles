FROM ubuntu:xenial  
MAINTAINER Mark Vermeulen <markhvermeulen@gmail.com>  
  
# Prevent dpkg errors  
ENV TERM=xterm-256color  
  
RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list  
  
# Install node.js  
RUN apt-get update && \  
apt-get install sudo -y && \  
apt-get install curl -y && \  
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \  
apt-get install -y node.js  
  
COPY . /app  
WORKDIR /app  
  
# Install application dependencies  
RUN npm install -g mocha && \  
npm install  
  
# Add entrypoint script  
ENTRYPOINT ["mocha"]  
  

