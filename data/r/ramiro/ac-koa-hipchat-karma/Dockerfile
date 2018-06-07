FROM node:latest  
MAINTAINER Atlassian Labs "https://botlab.hipch.at"  
COPY . /src  
RUN cd /src; npm install  
EXPOSE 8080  
CMD export MONGO_ENV=MONGO_URL; export
MONGO_URL="mongodb://$MONGO_PORT_27017_TCP_ADDR:27017/ac"; node --harmony
/src/web.js  
  

