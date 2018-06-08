FROM node:latest  
MAINTAINER Mohd Faiz Hasim <faiz.hasim@servicerocket.com>  
RUN mkdir -p /opt/sinopia/storage  
  
WORKDIR /opt/sinopia  
  
COPY package.json /opt/sinopia/package.json  
RUN npm install  
COPY config.yaml /opt/sinopia/config/config.yaml  
CMD ["node", "/opt/sinopia/node_modules/sinopia/bin/sinopia", "--config",
"/opt/sinopia/config/config.yaml"]  
EXPOSE 4873  
VOLUME ["/opt/sinopia/storage", "/opt/sinopia/config"]

