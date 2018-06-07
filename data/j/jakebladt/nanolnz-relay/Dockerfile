FROM node:boron  
MAINTAINER jake@jakebladt.com  
  
WORKDIR /relayserver  
COPY . /relayserver  
EXPOSE 5000:5000  
RUN npm install  
CMD ["node", "server.js"]  

