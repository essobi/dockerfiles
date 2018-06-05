FROM node:8.7.0  
WORKDIR /usr/src/app  
  
COPY package.json .  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 3000:3000  
CMD ["npm", "start"]  

