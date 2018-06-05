############################################################  
# Dockerfile to build Red White and Brew Website Node App  
# Based on Node  
############################################################  
  
FROM node:4-onbuild  
  
MAINTAINER Erik Hage <ehage4@gmail.com>  
  
#Setting ENV variables  
ENV TERM xterm  
  
#Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
#Install App Dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
#Install text editor nano  
RUN ["apt-get", "update"]  
RUN ["apt-get", "install", "-y", "nano"]  
  
#Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  
  

