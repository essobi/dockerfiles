FROM node:boron  
WORKDIR /usr/src/app  
COPY package.json .  
COPY src/ /usr/src/app/  
RUN npm config set strict-ssl false  
RUN npm install  
  
EXPOSE 3000  
CMD [ "node", "/usr/src/app/index.js" ]  
  

