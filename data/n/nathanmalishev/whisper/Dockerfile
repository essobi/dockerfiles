FROM node:7-slim  
  
MAINTAINER Nathan Malishev  
  
COPY . /privatequestions  
WORKDIR /privatequestions  
  
#Packages  
RUN apt-get update -q  
  
##NPM global packages  
RUN npm install -g forever  
RUN npm install  
  
# Provides cached layer for node_modules  
ADD package.json /tmp/package.json  
RUN cd /tmp && yarn  
RUN mkdir -p /src && cp -a /tmp/node_modules /src/  
  
#Create node logging folder  
RUN mkdir -p /var/log/nodejs  
  
CMD ["npm","start"]  

