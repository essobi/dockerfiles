# Base image  
FROM node:boron  
  
# App dir  
WORKDIR /usr/src/app  
  
COPY package.json .  
COPY package.json package-lock.json  
  
RUN npm install  
  
# Bundle app source  
COPY . .  
  
EXPOSE 8080  
CMD [ "npm", "start"]  

