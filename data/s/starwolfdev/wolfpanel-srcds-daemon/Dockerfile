FROM node:8-alpine  
  
WORKDIR /usr/src/daemon  
  
COPY package*.json ./  
  
RUN npm install --only=production  
  
COPY . .  
  
CMD npm run start

