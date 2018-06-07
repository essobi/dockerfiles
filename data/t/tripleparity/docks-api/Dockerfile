FROM node:9.8.0-alpine  
  
MAINTAINER TripleParity  
  
RUN apk add --update python make g++  
  
EXPOSE 8080  
WORKDIR /app  
  
COPY package*.json ./  
RUN npm install --only=production  
  
COPY . .  
  
CMD ./scripts/docks-prod-start.sh  

