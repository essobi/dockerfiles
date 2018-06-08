FROM python:2.7-slim  
MAINTAINER Truman Woo <chunan.woo@gmail.com>  
  
# Install Node.js and make tools  
RUN apt-get update && apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN apt-get install -y build-essential  
  
# Install node.js associated modules  
# RUN npm install -g cnpm --registry=https://registry.npm.taobao.org  
RUN npm install -g sails  
RUN npm install -g grunt-cli  
RUN npm install -g pm2  
  
# Install pm2-slack integration  
RUN pm2 install pm2-slack  
RUN pm2 set pm2-slack:restart true  
RUN pm2 set pm2-slack:stop true  
  
# Setup default work dir  
WORKDIR /  

