FROM node:6.9.1  
RUN npm i -g babel-cli nodemon  
  
COPY designer/package.json /usr/src/app/  
  
WORKDIR /usr/src/app  
  
RUN npm install  
  
COPY shared /usr/src/shared  
COPY designer/. /usr/src/app/  
  
RUN npm run build  
  
CMD nodemon ./scripts/server.js --env docker --watch src

