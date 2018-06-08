FROM node:8-alpine  
  
USER node  
RUN mkdir -p /home/node/app  
WORKDIR /home/node/app  
COPY package.json package-lock.json ./  
  
USER root  
COPY . .  
RUN chown -R node:node /home/node/app  
  
USER node  
RUN npm install  
  
EXPOSE 3000  

