# DOC BUILD  
FROM node:8.9.4-alpine as builder  
  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
  
RUN npm i  
  
# RUN npm i --registry=https://registry.npm.taobao.org  
COPY . /usr/src/app  
  
RUN npm run build  
  
# DOC DEPLOY  
FROM nginx:stable-alpine  
  
WORKDIR /usr/share/nginx/html  
  
RUN rm *.*  
  
COPY \--from=builder /usr/src/app/build/ ./  
  
COPY ext/default.conf /etc/nginx/conf.d/default.conf

