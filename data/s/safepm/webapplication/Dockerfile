FROM node:carbon  
  
# Create app directory  
WORKDIR /app  
  
COPY package*.json ./  
RUN npm install  
  
# Bundle app source  
COPY . .  
RUN npm run build  
EXPOSE 8080  
CMD [ "npm", "run", "server" ]

