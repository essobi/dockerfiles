FROM node:8.6-alpine  
WORKDIR /files  
CMD ["/usr/local/bin/node", "server/server.js"]  
EXPOSE 8888  
  
ADD package.json /files/package.json  
ADD server /files/server  
ADD shared /files/shared  
ADD test /files/test  
RUN cd /files && npm install  

