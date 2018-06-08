FROM node:6-alpine  
  
MAINTAINER omercnet "git@omer.io"  
RUN npm install -g standard && \  
npm install -g standard-reporter && \  
npm cache clean && \  
mkdir /standard  
  
WORKDIR /standard  
  
VOLUME /standard  
  

