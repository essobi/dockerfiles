FROM node:carbon  
  
WORKDIR /usr/src/app  
  
# Install app dependencies  
# Use a wildcard to ensure both package.json AND package-lock.json are copied  
# where available (npm@5+)  
COPY package*.json ./  
RUN npm install  
  
# IF you are building your code for production  
# RUN npm install --only=production  
COPY . .  
  
EXPOSE 8081  
CMD ["npm", "start"]

