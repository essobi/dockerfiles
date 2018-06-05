FROM node:5.11  
MAINTAINER Kukua Team <dev@kukua.cc>  
  
WORKDIR /data  
COPY ./ /data/  
RUN npm install  
RUN npm run compile  
RUN npm prune --production  
  
EXPOSE 3000  
CMD npm start  

