FROM node:5.1  
MAINTAINER Kukua Team <dev@kukua.cc>  
  
WORKDIR /data  
COPY ./ /data/  
RUN npm install  
RUN npm run compile  
RUN npm prune --production  
RUN touch /tmp/output.log  
  
EXPOSE 3000  
CMD npm start  

