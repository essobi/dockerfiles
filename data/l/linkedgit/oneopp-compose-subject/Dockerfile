FROM node:8-alpine  
  
# Maintainer  
MAINTAINER Aksenchyk V. <aksenchyk.v@gmail.com>  
  
# Define app directory  
WORKDIR /usr/app  
  
# Create app directory  
RUN mkdir -p /usr/app  
  
# Copy app sources  
COPY . /usr/app  
  
# Install curl for swarm helthchecking  
RUN apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
# Install dependencies and build client  
RUN npm install  
  
# start command  
CMD [ "npm", "start" ]  
  
# Make server available  
EXPOSE 5027  

