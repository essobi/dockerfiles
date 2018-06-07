FROM node:7  
EXPOSE 3000 8000  
RUN npm install webpack -g  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY package.json package.json  
  
RUN npm install && npm cache clean  
  
# && webpack --config webpack.config.js  
COPY . .  
  
RUN npm run build  
  
CMD ["npm", "run", "prod:server"]  
  
#https://lockmedown.com/docker-for-developers-create-dev-image/

