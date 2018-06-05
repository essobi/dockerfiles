FROM node:carbon-
alpine@sha256:dcee83ad53ab1d2754ca7029a06aa1f2c79bf3ee08b1a40bb052443efacd3b8f  
  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
RUN npm install --only=production  
  
COPY . .  
  
CMD [ "npm", "start" ]  
  

