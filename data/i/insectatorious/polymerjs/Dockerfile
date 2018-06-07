FROM ubuntu:16.04  
MAINTAINER Sumanas Sarma <insectatorious+docker@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git  
  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y nodejs  
  
RUN npm install -g npm@latest  
  
RUN npm install -g \  
yarn \  
bower  
  
# See https://github.com/Polymer/polymer-cli/issues/832#issuecomment-362735226  
RUN yarn global add polymer-cli  
  
EXPOSE 8081  

