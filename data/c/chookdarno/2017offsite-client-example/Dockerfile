# Offical node https://hub.docker.com/_/node/  
# build: docker build -t cardano/2017offsite-client-example .  
#run: docker run -p 39000:8080 -d cardano/2017offsite-client-example  
FROM node:6.9.4  
MAINTAINER Cardano  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
ADD package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
ADD . /usr/src/app  
  
# app binds to port 8080 so you'll use the EXPOSE instruction to have it
mapped by the docker daemon  
EXPOSE 3000  
CMD [ "npm", "start" ]  

