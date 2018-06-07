FROM node:8.10.0-stretch  
  
WORKDIR /usr/src/dsc  
  
RUN apt-get install g++  
  
COPY package*.json ./  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 3000  
CMD [ "node", "index.js" ]  

