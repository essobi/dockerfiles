# Offical node https://hub.docker.com/_/node/  
# build: docker build -t cardano/2017offsite-service-example .  
#run: docker run -p 49000:8080 -d cardano/2017offsite-service-example  
FROM node:6.9.4  
  
MAINTAINER Cardano  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
ADD package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
ADD service /usr/src/app/service  
ADD tools /usr/src/app/tools  
ADD config /usr/src/app/config  
  
# app binds to port 8080 so you'll use the EXPOSE instruction to have it
mapped by the docker daemon  
EXPOSE 8080  
  
CMD [ "npm", "start" ]  

