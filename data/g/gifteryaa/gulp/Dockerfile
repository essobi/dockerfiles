FROM node:alpine  
  
RUN apk add --quiet --no-cache bash git && \  
yarn global add bower gulp && \  
yarn cache clean && \  
rm -rf /var/cache/* /tmp/*  
  
WORKDIR /app  

