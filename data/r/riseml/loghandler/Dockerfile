FROM node:8.4.0-alpine  
  
RUN npm -g install yarn  
  
RUN mkdir /app  
  
WORKDIR /app  
  
COPY package.json /app  
  
RUN yarn install  
  
RUN mkdir /log  
  
COPY . /app  
CMD node index.js

