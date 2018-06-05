FROM node:8  
WORKDIR /usr/src  
  
COPY package*.json ./  
  
RUN npm install  
  
COPY . .  
  
CMD [ "npm", "start" ]  

