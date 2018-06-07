FROM node:boron  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git && \  
apt-get clean && \  
npm install -g gulp bower polymer-cli generator-polymer-init-custom-build
express  
  
COPY . /usr/src/app  
COPY ./src /usr/src/app  
COPY ./bower_components /usr/src/app  
COPY ./images /usr/src/app  
  
EXPOSE 8081  
CMD [ "npm","start" ]  

