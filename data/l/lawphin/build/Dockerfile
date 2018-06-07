FROM node:5.5  
MAINTAINER Thaweesak C <thaweesak@lawphin.com>  
  
RUN apt-get update -y  
RUN apt-get install -y ruby python gcc g++ make build-essential  
RUN apt-get install -y libkrb5-dev  
RUN gem install sass  
  
RUN npm install -g bower node-gyp grunt  
RUN mkdir /usr/src/app  
RUN mkdir /usr/src/data  
ADD exist/node_modules /usr/src/data  
  
WORKDIR /usr/src/app  

