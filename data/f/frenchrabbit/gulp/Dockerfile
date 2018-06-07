FROM node:alpine  
  
MAINTAINER frenchrabbit <hello@frenchrabbit.ru>  
  
# @TODO install imagemin binaries globally  
RUN apk add --quiet --no-cache bash git && \  
yarn global add bower gulp && \  
yarn cache clean && \  
rm -rf /var/cache/* /tmp/*  

