FROM ubuntu:14.04  
# Update APT  
RUN apt-get update  
  
# Base stuff  
RUN apt-get install -y --force-yes curl build-essential  
RUN apt-get install -y --force-yes git  
  
# Install editors  
RUN apt-get install -y --force-yes vim nano  
  
# NodeJS 5.*  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -  
RUN apt-get install -y --force-yes nodejs  
  
# Install grunt & node-sass  
RUN npm install -g grunt-cli node-sass bower  
  
# Fix Bower run as root  
RUN echo "alias bower=\"bower --allow-root\"" >> /etc/bash.bashrc  
  
WORKDIR /src  
  

