FROM node:alpine  
  
# Create app directory  
WORKDIR /usr/src/ao01  
  
# Install app dependencies  
COPY package.json .  
  
RUN npm install  
  
# Bundle app  
COPY . .  
  
EXPOSE 3000  
CMD ["npm", "start"]  

