FROM node:5  
MAINTAINER Octoblu, Inc. <docker@octoblu.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm -s install --production  
COPY . /usr/src/app/  
  
CMD [ "node", "--max-old-space-size=450", "command.js" ]  

