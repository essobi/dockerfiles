FROM node:carbon  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
RUN npm install  
  
COPY . .  
  
RUN npm run postinstall  
  
EXPOSE 8080  
CMD ["npm", "start"]

