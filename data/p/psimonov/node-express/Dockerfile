FROM node:alpine  
  
WORKDIR /usr/src/node-express  
  
COPY package.json ./  
  
RUN yarn global add nodemon  
RUN yarn install  
  
COPY app ./app/  
COPY app ./app/  
  
EXPOSE 3000  
CMD [ "nodemon", "app/server.js" ]  

