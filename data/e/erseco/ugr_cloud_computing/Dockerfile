# Using the LTS 8.x version of node docker container (in Debian 8.10)  
FROM node:carbon  
  
MAINTAINER Ernesto Serrano <erseco@correo.ugr.es>  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
RUN npm install  
# If you are building your code for production  
# RUN npm install --only=production  
# Bundle app source  
COPY . .  
  
EXPOSE 80  
CMD [ "npm", "start" ]  

