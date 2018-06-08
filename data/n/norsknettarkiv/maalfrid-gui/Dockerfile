FROM node:8-alpine  
  
ARG BASE_HREF=/maalfrid  
ARG DEPLOY_URL=/maalfrid  
  
COPY package.json yarn.lock /usr/src/app/  
WORKDIR /usr/src/app  
RUN yarn install  
  
COPY . .  
RUN node_modules/@angular/cli/bin/ng build --configuration=production  
  
FROM nginx:alpine  
LABEL maintainer="nettarkivet@nb.no"  
  
ARG DEPLOY_URL=/maalfrid  
  
COPY \--from=0 /usr/src/app/dist/ /usr/share/nginx/html${DEPLOY_URL}  
  
COPY nginx/default.conf /etc/nginx/conf.d/  
  

