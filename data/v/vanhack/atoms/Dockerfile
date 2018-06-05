FROM node:boron  
  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN cd /usr/src/app && npm install --production  
COPY . /usr/src/app

