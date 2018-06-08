FROM node:slim  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY .npmrc package.json package-lock.json ./  
  
RUN npm install  
# If you are building your code for production  
# RUN npm install --only=production  
# Bundle app source  
COPY . .  
  
# Build bundle  
# RUN npm run build  
EXPOSE 8080  
CMD [ "npm", "start" ]  

