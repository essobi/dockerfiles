FROM node:alpine  
MAINTAINER Raymond Wen  
  
ENV HUGO_VERSION 0.31.1  
RUN apk update && apk add ca-certificates openssl wget curl tidyhtml make &&
update-ca-certificates  
RUN wget
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz  
RUN tar xvf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz  
RUN mv hugo /usr/local/bin  
RUN rm hugo_${HUGO_VERSION}_Linux-64bit.tar.gz  
RUN npm add -g csslint jshint eslint htmllint-cli uglify-js uglifycss standard
prettier  

