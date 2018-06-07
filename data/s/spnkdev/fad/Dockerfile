FROM ubuntu:latest  
MAINTAINER spnkdev  
  
RUN apt-get update  
RUN apt-get install -y nodejs nodejs-legacy npm  
  
COPY package.json FBWebsite/  
  
COPY . FBWebsite/  
RUN cd FBWebsite && npm install && npm install forever -g  
WORKDIR FBWebsite/  
  
EXPOSE 3000

