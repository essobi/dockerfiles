FROM node:carbon  
  
WORKDIR /usr/src/app  
COPY package*.json ./  
RUN npm install --registry=https://registry.npm.taobao.org  
COPY . .  
RUN npm run build  
EXPOSE 8080  
CMD [ "npm", "start" ]  

