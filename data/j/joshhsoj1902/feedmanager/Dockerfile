FROM node:6.2.2-wheezy  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update  
RUN apt-get -y install build-essential  
RUN npm install -g node-gyp  
  
COPY app/package.json /usr/src/app/  
RUN npm install  
  
ADD app /usr/src/app  
RUN npm install  
  
CMD [ "node", "server.js" ]  

