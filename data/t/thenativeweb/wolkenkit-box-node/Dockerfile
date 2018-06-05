FROM node:8.9.1-alpine  
MAINTAINER the native web <hello@thenativeweb.io>  
  
ADD ./keys /keys/  
  
RUN apk update && \  
apk upgrade && \  
apk add git openssl && \  
wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \  
chmod a+x /usr/local/bin/dumb-init  

