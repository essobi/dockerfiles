FROM node:8.7.0  
ENV NODE_ENV=production  
  
COPY package.json /var/www/main/package.json  
  
COPY package-lock.json /var/www/main/package-lock.json  
  
WORKDIR /var/www/main  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 4000  
CMD ["node", "./bin/www"]  

