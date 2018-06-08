FROM node:alpine  
  
# Maintainer  
MAINTAINER Aksenchyk V. <aksenchyk.v@gmail.com>  
  
# Define app directory  
WORKDIR /usr/src/app  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
  
# Install curl for swarm helthchecking  
RUN apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
# Copy app sources  
COPY . /usr/src/app  
  
# Install dependencies and build client  
RUN npm install  
  
# start command  
CMD [ "npm", "start" ]  
  
# Make server and client available  
EXPOSE 3000  

