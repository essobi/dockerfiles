FROM node:8  
# Create app directory  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
RUN npm install  
  
# Bundle app source  
COPY . .  
  
EXPOSE 8000  
CMD [ "npm", "start" ]  

