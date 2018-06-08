FROM node:6-alpine  
  
LABEL MAINTAINER Shiyu Han <dock@moyo.im>  
  
RUN apk add --update --virtual builds python make g++  
  
RUN npm install -g log.io --user 'root'  
  
RUN apk del builds && rm -rf /var/cache/apk/* /tmp/*  

