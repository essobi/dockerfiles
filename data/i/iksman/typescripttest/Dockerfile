FROM node:latest  
WORKDIR /app  
  
COPY package.json /app/  
  
RUN npm install  
  
COPY . .  
RUN npm run-script compile  
  
CMD npm run-script startNode

