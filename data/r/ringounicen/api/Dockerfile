FROM node:0.10  
MAINTAINER "Pablo Saavedra"  
RUN mkdir /app  
ADD package.json /app/package.json  
ADD util /app/util  
ADD mappings /app/mappings  
ADD server.js /app/server.js  
ADD routes /app/routes  
  
WORKDIR /app  
RUN npm install --production  
  
CMD node server.js  
  

