# VERSION 1.0.1  
# AUTHOR: Jhen <developer@jhen.me>  
# DESCRIPTION: Thumbd image based on mhart/alpine-node  
# TO_BUILD: docker build --rm -t fucompany/thumbd .  
# SOURCE: https://github.com/mybigday/docker-thumbd  
FROM mhart/alpine-node:6  
MAINTAINER Jhen <developer@jhen.me>  
  
ADD start /start  
  
# Install imagemagick & pm2 & thumbd  
RUN apk update && \  
apk add imagemagick && \  
rm -rf /var/cache/apk/* && \  
npm set registry https://registry.npmjs.org && \  
npm install -g pm2 @fugood/thumbd@2.19.1 && \  
npm cache clear && \  
chmod 755 /start  
  
CMD ["sh", "/start"]  

