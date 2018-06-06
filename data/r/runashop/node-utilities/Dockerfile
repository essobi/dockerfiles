FROM node:alpine  
  
RUN set -xe && \  
apk add --update git && \  
yarn global add --prefix /usr/local grunt-cli && \  
mkdir -p /var/www  
  
WORKDIR /var/www

