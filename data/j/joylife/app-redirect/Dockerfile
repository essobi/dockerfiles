FROM node:6.9.4  
MAINTAINER Joy Life Services <services@withjoy.com>  
  
COPY ./package.json ./usr/src/app/package.json  
RUN cd ./usr/src/app && npm install  
  
COPY . ./usr/src/app  
  
CMD cd ./usr/src/app && npm start  
  

