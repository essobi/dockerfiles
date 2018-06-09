FROM node:carbon  
  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
RUN npm install  
  
COPY . .  
EXPOSE 8080  
ENV DEBUG oidc-provider*  
  
CMD ["node", "index.js"]

