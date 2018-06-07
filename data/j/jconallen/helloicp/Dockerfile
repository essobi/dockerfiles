FROM node:10-alpine  
  
CMD mkdir /app  
WORKDIR /app  
  
COPY app.js .  
COPY LICENSE .  
COPY package.json .  
COPY README.md .  
COPY views ./views  
  
RUN npm install  
  
EXPOSE 3000  
CMD ["node", "app.js"]  

