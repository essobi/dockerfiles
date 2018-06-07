# Start from official Node image  
FROM node:8.1.2  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Copy App Over  
COPY . /usr/src/app/  
RUN npm install  
  
# Start the bot  
CMD [ "npm", "start" ]  

