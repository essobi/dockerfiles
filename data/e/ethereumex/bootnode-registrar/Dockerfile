FROM node:9.2.1  
WORKDIR /var/lib/bootnode  
COPY package*.json ./  
RUN npm install --production  
  
COPY . .  
EXPOSE 3000  
CMD [ "node", "app.js" ]

