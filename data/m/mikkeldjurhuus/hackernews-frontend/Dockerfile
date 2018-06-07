FROM node:boron  
  
# Create app directory  
RUN mkdir -p /website/src/app  
  
WORKDIR /website/src/app  
  
# Bundle app source  
COPY . .  
  
RUN npm install  
  
CMD [ "npm", "start" ]  
  
EXPOSE 8080

