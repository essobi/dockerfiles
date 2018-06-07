FROM node:4.4.7  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD package.json /usr/src/app/  
RUN npm install  
ADD . /usr/src/app  
  
EXPOSE 3000  
CMD [ "node", "server.js" ]  

