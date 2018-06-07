FROM node:slim  
  
MAINTAINER Zack YL Shih <zackyl.shih@moxa.com>  
  
COPY . /data  
WORKDIR /data  
  
RUN npm install --production  
  
EXPOSE 8080  
CMD npm start  

