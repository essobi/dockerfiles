FROM node:slim  
  
RUN apt-get update && apt-get -y install unzip  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
  

