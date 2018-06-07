FROM node:7  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json .  
  
RUN npm install  
  
# Bundle app source  
COPY . .  
  
EXPOSE 3002  
CMD ["node", "server.js"]

