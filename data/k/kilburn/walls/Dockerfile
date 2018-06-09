FROM node:carbon-alpine  
  
WORKDIR /home/node  
  
COPY package*.json ./  
RUN npm install --production  
  
COPY config*.js ./  
COPY lib/ ./lib/  
  
EXPOSE 12177  
CMD [ "npm", "start" ]  

