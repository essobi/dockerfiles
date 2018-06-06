FROM node:alpine  
  
# Maintainer  
MAINTAINER Aksenchyk V. <aksenchyk.v@gmail.com>  
  
# Define app directory  
WORKDIR /usr/src/app  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
  
# Copy app sources  
COPY . /usr/src/app  
  
# Install dependencies and build client  
RUN npm install  
  
# Make server and client available  
EXPOSE 4032  
CMD [ "npm", "start"]

