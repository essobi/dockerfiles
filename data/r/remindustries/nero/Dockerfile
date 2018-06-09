FROM node:7.10.0-alpine  
LABEL maintainer Wolke "wolke@ram.moe"  
WORKDIR /usr/src  
RUN mkdir nero  
WORKDIR /  
COPY . /usr/src/nero  
WORKDIR /usr/src/nero  
RUN npm config set registry http://registry.npmjs.org/ && npm install  
RUN npm install  
EXPOSE 8080  
ENTRYPOINT [ "node", "index.js" ]

