FROM node:6.11.4-alpine  
MAINTAINER Wonderlic DevOps <DevOps@wonderlic.com>  
  
COPY ccc-streamer-utilities.js quotes.js server.js package.json /app/  
  
RUN cd /app && \  
npm install --production && \  
ln -s /usr/local/bin/node /app/crypto-api  
  
CMD ["/app/crypto-api", "/app/server.js"]  

