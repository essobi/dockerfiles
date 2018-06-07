FROM node:6.7-slim  
  
MAINTAINER Thomas Krampl  
  
ENV EMBER_CLI_VERSION 2.9.0-beta.2  
  
RUN apt-get update -y && \  
apt-get install -y git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN npm install -g --quiet ember-cli@$EMBER_CLI_VERSION bower && npm cache
clean  

