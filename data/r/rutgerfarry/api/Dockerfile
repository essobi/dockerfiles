# Build stage  
FROM node:8  
WORKDIR /usr/src  
  
COPY package*.json ./  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 5000  
CMD ["npm", "start"]  

