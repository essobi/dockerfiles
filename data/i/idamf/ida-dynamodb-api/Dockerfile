FROM node:9.1-slim  
  
WORKDIR /app  
  
ENV NODE_ENV production  
  
COPY package.json /app/package.json  
COPY api-server.js /app/api-server.js  
  
RUN npm install  
  
ENTRYPOINT ["node","api-server.js"]

