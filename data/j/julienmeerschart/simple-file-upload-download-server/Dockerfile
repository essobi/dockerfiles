FROM node:8.6.0-alpine  
COPY server.js /file/server.js  
COPY package.json /file/package.json  
RUN cd /file && npm install  
ENTRYPOINT ["node","/file/server.js","3000","/tmp"]

