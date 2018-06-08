FROM node:8.7.0-alpine  
  
WORKDIR /app  
  
COPY package.json package.json  
COPY package-lock.json package-lockjson  
RUN npm install  
  
COPY bin bin  
COPY src src  
COPY .babelrc .babelrc  
  
RUN npm run build  
  
EXPOSE 3000  
CMD node bin/server.js

