FROM node:8.11.2-alpine  
MAINTAINER "contact@koumoul.com"  
RUN apk add --update curl git  
# RUN npm i npm@latest -g  
# Install node-prune to reduce size of node_modules  
RUN curl -sfL https://install.goreleaser.com/github.com/tj/node-prune.sh | sh
-s -- -b /usr/local/bin  
  
# Install common packages so that later npm install run faster  
ENV NODE_ENV production  
WORKDIR /webapp  
ADD package.json .  
RUN npm install && node-prune  
RUN rm package.json  

