#########################################################################  
#  
# Mailheap.io microservice to render and send templated messages  
#  
# Build with:  
# docker build -t="tuyakhov/loopback" .  
#  
# https://hub.docker.com/_/node/  
#  
########################################################################  
  
# Base from official nodejs image  
FROM node:5.11  
  
# Install strongloop  
RUN npm install -g strongloop  
# Install nodemon for development use  
RUN npm install -g nodemon  
# Install mocha for testing  
RUN npm install -g mocha  
  
EXPOSE 3000 51459  

