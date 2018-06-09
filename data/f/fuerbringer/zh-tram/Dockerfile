# Image details  
FROM node:carbon  
  
# Prepare app data  
WORKDIR /usr/src/app  
COPY package*.json ./  
RUN npm install  
COPY . .  
  
# Run  
EXPOSE 3000  
CMD [ "npm", "start" ]  

