FROM node  
  
WORKDIR /app  
  
COPY ./package*.json ./  
  
RUN npm install --production  
  
COPY . .  
  
CMD ["node", "server.js"]  
  
EXPOSE 3000  

