FROM node:boron  
MAINTAINER jake@jakebladt.com  
  
WORKDIR /restserver  
COPY . /restserver  
EXPOSE 9001:9001  
RUN npm install  
CMD ["node", "api.js"]  

