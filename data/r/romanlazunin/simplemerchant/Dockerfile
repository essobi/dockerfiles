FROM node:carbon  
  
WORKDIR /user/rowan/  
  
COPY package*.json ./  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

