FROM ubuntu:14.04  
MAINTAINER Spencer Herzberg <spencer.herzberg@gmail.com>  
  
RUN apt-get update -qq && apt-get install -y software-properties-common  
  
RUN apt-add-repository ppa:chris-lea/node.js  
  
RUN apt-get update -qq && apt-get install -y nodejs  
  
RUN npm install -g elasticdump  
  
ENTRYPOINT ["/usr/bin/elasticdump"]  

