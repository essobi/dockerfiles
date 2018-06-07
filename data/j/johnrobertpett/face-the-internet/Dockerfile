# VERSION 0.2  
# DOCKER-VERSION 0.3.4  
# To build:  
# 1. Install docker (http://docker.io)  
# 2. Build container: docker build .  
# Pull image for specific node version (https://github.com/nodejs/docker-node)  
FROM node:0.10  
# Expose the ports that your app uses. For example:  
EXPOSE 3000  
# Set environment variables.  
ENV HOME /root  
# map files to '/app' inside the docker container  
ADD . /app  
# Define working directory.  
WORKDIR /app  
# Install app dependencies  
RUN npm install  
  
# Define default command.  
CMD ["bash", "node /app/index.js"]  

