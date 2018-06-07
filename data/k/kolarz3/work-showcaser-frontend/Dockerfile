FROM node:alpine  
  
WORKDIR /usr/src/app  
  
COPY package.json ./  
  
RUN npm install  
  
RUN npm i -g http-server  
  
COPY . .  
  
CMD [ "npm", "run", "prod" ]

