# Start from the base image  
FROM ubuntu:16.04  
MAINTAINER Marcela Rodriguez <marcela@cantina.co>  
  
# Install some boilerplate dependencies  
RUN apt-key update && apt-get update && apt-get install -y curl build-
essential libssl-dev nano man git wget python ntp libkrb5-dev  
  
# Install NVM  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh |
bash  
  
# Using bash, we install node v8.9.4, set it to our default, and use it  
RUN ["/bin/bash", "-c", "source /root/.nvm/nvm.sh && nvm install v8.9.4 && nvm
alias default v8.9.4 && nvm use default && npm install -g grunt-cli forever
json"]  

