FROM ubuntu:17.04  
FROM node:6.10.3  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN npm install  
RUN npm install date-and-time --save  
RUN npm install --save body-parser  
RUN npm install cors  
RUN npm install mysql  
CMD ["node", "app.js"]  
  

