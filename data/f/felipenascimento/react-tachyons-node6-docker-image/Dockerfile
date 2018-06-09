# FROM node:6-slim  
FROM mhart/alpine-node:6.10.2  
# Create app directory  
RUN mkdir -p /usr/app  
WORKDIR /usr/app  
  
COPY package.json /usr/app  
RUN npm i  

