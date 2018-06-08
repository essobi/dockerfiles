FROM node:8.9-alpine  
  
  
WORKDIR /usr/src/http-mailer  
COPY package*.json ./  
RUN npm install  
COPY . .  
EXPOSE 8025  
CMD ["node", "src/index.js"]  

