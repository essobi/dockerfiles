FROM node:6.11.4-alpine  
MAINTAINER Wonderlic DevOps <DevOps@wonderlic.com>  
  
COPY config.js handlers.js server.js package.json /app/  
  
RUN cd /app && \  
npm install --production && \  
ln -s /usr/local/bin/node /app/s3-spa-loader  
  
CMD ["/app/s3-spa-loader", "/app/server.js"]  

