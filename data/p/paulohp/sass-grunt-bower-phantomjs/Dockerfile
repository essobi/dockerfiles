FROM mhart/alpine-node:5.8  
MAINTAINER Paulo Pires @paulohp  
  
# Install base packages  
RUN apk update  
RUN apk upgrade  
RUN apk add wget bash git g++ python make tar  
  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  
RUN rm -rf /tmp/**  
  
RUN \  
npm install -g grunt-cli && \  
npm install -g bower  
  
ADD package.json /tmp/package.json  
ADD .npmrc /tmp/.npmrc  
  
RUN cd /tmp && npm install  

