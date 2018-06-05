###########################################  
# Dockerfile to build a Node.JS REST service  
###########################################  
# Base image is Ubuntu  
FROM node:argon  
# Author: robymes  
MAINTAINER robymes <robymes@gmail.com>  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
# Bundle app source  
COPY . /usr/src/app  
EXPOSE 80  
CMD [ "npm", "start" ]

