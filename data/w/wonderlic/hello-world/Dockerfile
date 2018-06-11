FROM node:6.11.4-alpine  
MAINTAINER Wonderlic DevOps <DevOps@wonderlic.com>  
  
COPY server.js /app/server.js  
  
RUN ln -s /usr/local/bin/node /app/hello-world  
  
CMD ["/app/hello-world", "/app/server.js"]  

