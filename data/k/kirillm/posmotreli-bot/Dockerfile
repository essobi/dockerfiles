FROM node:8-alpine  
  
ADD ./package.json /opt/app/package.json  
  
WORKDIR /opt/app  
  
RUN npm install  
  
ADD . /opt/app  
  
CMD node index.js

