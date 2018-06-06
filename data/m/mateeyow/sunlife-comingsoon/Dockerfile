FROM node:6.2.2-wheezy  
  
MAINTAINER Matthew Torres <matthew.torres211@gmail.com>  
  
WORKDIR /app  
  
COPY package.json .  
  
RUN npm i  
  
COPY . .  
  
EXPOSE 8000  
CMD ["node", "index.js"]

