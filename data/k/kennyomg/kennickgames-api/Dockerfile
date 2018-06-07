FROM node:6.3  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
  
COPY . /usr/src/app  
  
ENV API_PORT 8080  
EXPOSE $API_PORT  
  
CMD [ "node", "server.js" ]  

