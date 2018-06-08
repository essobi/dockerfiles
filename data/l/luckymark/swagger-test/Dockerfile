FROM node:8.6.0-alpine  
  
WORKDIR /home  
  
RUN npm install -g mocha typescript  
  
COPY . /home  
  
RUN npm install  
  
RUN tsc  
  

