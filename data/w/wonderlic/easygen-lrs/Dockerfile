FROM node:4.8.4-slim  
MAINTAINER Wonderlic DevOps <DevOps@wonderlic.com>  
  
COPY commands /app/commands  
COPY db /app/db  
COPY helpers /app/helpers  
COPY middlewares /app/middlewares  
COPY migration /app/migration  
COPY routeHandlers /app/routeHandlers  
COPY utils /app/utils  
COPY app.js constants.js queryParser.js package.json /app/  
  
RUN cd /app && \  
npm install --production && \  
ln -s /usr/local/bin/node /app/easygen-lrs  
  
CMD ["/app/easygen-lrs", "/app/app.js"]  

