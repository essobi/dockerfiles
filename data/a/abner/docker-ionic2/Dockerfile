FROM node:6.9.5-alpine  
MAINTAINER abner <contato@abner.io>  
  
RUN apk add \--no-cache ca-certificates python=2.7.12-r0 make gcc g++ build-
base  
  
RUN npm config set cache /cache/.npm/  
  
RUN npm install -g yarn  
  
RUN yarn config set cache-folder /cache/yarn  
  
RUN yarn global add "ionic@2.2.1" node-sass@3.10.1  
  

