FROM node:alpine  
  
MAINTAINER Travix  
  
RUN apk --no-cache add bash \  
&& rm -rf /var/cache/apk/*  
  
COPY index.js /app/  
  
ENTRYPOINT node /app/index.js  

